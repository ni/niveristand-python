import ast
import inspect
import os
import tempfile

from niveristand import _errormessages
from niveristand._translation import utils
from niveristand._translation.py2rtseq.utils import Resources
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.clientapi import rtsequencedefinitionutils as rtsequtils
from niveristand.errors import TranslateError, VeristandError
from NationalInstruments.VeriStand.Data import SystemDefinitionChannelResource  # noqa: E501, I100 We need these C# imports to be out of order.
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ChannelReferenceDeclaration, ChannelSizeType
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import EvaluationMethod
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ParameterDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Reference
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import References


class RealTimeSequence:
    """
    A real-time sequence that can run on the VeriStand Engine.

    Args:
        top_level_func: the function to transform.
        rtseq_pkg(:class:`RealTimeSequencePackage`): the containing package in case you want to add this sequence to a
                                                    library.

    Raises:
        :class:`niveristand.errors.TranslateError`: if translation fails.
        :class:`niveristand.errors.VeristandError`: if compilation fails.

    """

    def __init__(self, top_level_func, rtseq_pkg=None):
        self._top_level_func = top_level_func
        self._path = ''
        self._rtseq = None
        self._rtseqpkg = rtseq_pkg
        self._ref = None
        # finally, initialize the transform
        self._transform()

    def run(self, rtseq_params={}):
        """
        Runs the sequence on the globally configured VeriStand Engine.

        Args:
            rtseq_params (Dict[str, niveristand.clientapi._datatypes.rtprimitives.DoubleValue]):  the parameters to be
             passed to the RT sequence.

        Returns:
            niveristand.clientapi.stimulusprofileapi.StimulusProfileState: Stimulus profile session state.

        Deploys and runs the sequence without waiting for the sequence to finish. Use the returned
        :class:`StimulusProfileState` to wait for the sequence to complete and obtain the return value.

        For a simpler use case, refer to :func:`niveristand.realtimesequencetools.run_py_as_rtseq`

        """
        if self._rtseq is None:
            raise VeristandError(_errormessages.run_without_valid_sequence)
        if self._path is None:
            raise VeristandError(_errormessages.invalid_path_for_sequence)

        name = self._build_file_name()
        return rtseqapi.run_rt_sequence(name, rtseq_params)

    def save(self, path=None):
        """
        Saves this sequence to disk.

        Args:
            path(Optional[str]): path to the location you want to save the sequence file.

        Returns:
            path you specify in **path**.

        All dependencies required for deployment of this sequence save to the same path.
        If you do not specify a path in **path**, this sequence saves to the location where you last saved the object.
        If you did not previously save the object, it saves to a temporary folder.

        For a simpler use case, refer to :func:`niveristand.realtimesequencetools.save_py_as_rtseq`

        """
        if self._rtseq is None:
            raise VeristandError(_errormessages.save_without_valid_sequence)
        if path is not None:
            self._path = os.path.abspath(path)
        elif not os.path.isdir(self._path):
            self._path = tempfile.mkdtemp()

        name = self._build_file_name()
        self._rtseqpkg.save_referenced(self._path, self)
        self._update_references()
        rtseqapi.save_real_time_sequence(self._rtseq, name)
        return name

    def _transform(self):
        from niveristand._decorators import rt_seq_mode_id
        real_obj = getattr(self._top_level_func, rt_seq_mode_id, None)
        if real_obj is None:
            raise TranslateError(_errormessages.invalid_top_level_func)
        src = inspect.getsource(real_obj)
        top_node = ast.parse(src)
        try:
            func_node = top_node.body[0]
        except TypeError:
            func_node = None
        if func_node is None or not isinstance(func_node, ast.FunctionDef):
            raise TranslateError(_errormessages.invalid_top_level_func)

        self._rtseq = rtseqapi.create_real_time_sequence()
        transform_resources = Resources(self._rtseq, str(self))
        if self._rtseqpkg is not None:
            transform_resources.set_dependency_pkg(self._rtseqpkg)
        utils.generic_ast_node_transform(func_node, transform_resources)
        self._rtseqpkg = transform_resources.get_dependency_pkg()
        self._rtseqpkg.append(inspect.getmodule(real_obj))
        self._update_parameters(transform_resources.get_parameters())
        self._update_channel_refs(transform_resources.get_all_channel_refs())
        self.save()
        rtsequtils.compile_rtseq(self._rtseq)

    def _update_references(self):
        self._ref = Reference(str(self), self._build_file_name())
        self._rtseq.References = References()
        for referenced in self._rtseqpkg.get_referenced(self):
            self._rtseq.References.AddReference(referenced.get_reference())

    def _update_parameters(self, param_list):
        self._rtseq.Variables.Parameters.ClearParameters()
        for param in param_list:
            real_default = param.default_value._data_value
            real_eval_method = EvaluationMethod.ByValue if param.by_value else EvaluationMethod.ByReference
            real_param = ParameterDeclaration(param.rtseq_name, real_default, real_eval_method)
            self._rtseq.Variables.Parameters.AddParameter(real_param)

    def _update_channel_refs(self, channel_ref_list):
        self._rtseq.Variables.ChannelReferences.ClearChannelReferences()
        for channel_ref_obj in channel_ref_list:
            if channel_ref_obj.channel_is_vector:
                size_argument = ChannelSizeType.Vector
            else:
                size_argument = ChannelSizeType.Scalar
            system_definition_channel_resource = SystemDefinitionChannelResource(channel_ref_obj.channel_name)
            channel_reference_declaration = ChannelReferenceDeclaration(channel_ref_obj.rtseq_name,
                                                                        system_definition_channel_resource,
                                                                        size_argument)
            self._rtseq.Variables.ChannelReferences.AddChannelReference(channel_reference_declaration)

    def _build_file_name(self):
        return os.path.join(self._path, str(self) + ".nivsseq")

    def get_reference(self):
        return self._ref

    def __str__(self):
        return self._top_level_func.__name__
