"""Module for NationalInstruments.VeriStand.SystemStorage."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemStorage")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemStorage  # type: ignore
import System  # type: ignore

from .. import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.systemstorage.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemstorage.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class BaseNodeType(_DotNetBase):
    """Base class for all nodes in the tree. All actual nodes in the tree is a specialized type of this base class."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: BaseNodeType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.BaseNodeType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.BaseNodeType(*_unwrap(None, *args))

    @property
    def node_path_array(self) -> Sequence[str]:
        """Get the node path of the node as path array."""
        return _wrap(self._dotnet_instance.NodePathArray)

    @property
    def node_path(self) -> str:
        """Get the node path of the node as a string."""
        return _wrap(self._dotnet_instance.NodePath)

    @property
    def errors_array(self) -> Sequence[ErrorEntry]:
        return _wrap(self._dotnet_instance.ErrorsArray)

    @errors_array.setter
    def errors_array(self, value: Sequence[ErrorEntry]):
        self._dotnet_instance.ErrorsArray = next(_unwrap(None, value))

    @property
    def bfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return a Breath First Search enumerator. This enumerator iterates through all children of
            then node directly before diving into the hierarchy. For leaf type nodes it will return only itself."""
        return _wrap(self._dotnet_instance.BFSEnumerator)

    @property
    def dfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return a Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found."""
        return _wrap(self._dotnet_instance.DFSEnumerator)

    @property
    def child_only_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return enumerator that allow user to enumerate through the children of this node only."""
        return _wrap(self._dotnet_instance.ChildOnlyEnumerator)

    @property
    def child_only_object_enumerator(self) -> System.Collections.IEnumerator:
        """Return non generic enumerator that allow user to enumerate through the children of this node only."""
        return _wrap(self._dotnet_instance.ChildOnlyObjectEnumerator)

    @property
    def trav_parent_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return enumerator that allow user to enumerate through the parent."""
        return _wrap(self._dotnet_instance.TravParentEnumerator)

    @property
    def id(self) -> int:
        """ID"""
        return _wrap(self._dotnet_instance.ID)

    @id.setter
    def id(self, value: int):
        """ID"""
        self._dotnet_instance.ID = next(_unwrap(None, value))

    @property
    def temp_properties(self) -> Sequence[PropertyType]:
        return _wrap(self._dotnet_instance.TempProperties)

    @temp_properties.setter
    def temp_properties(self, value: Sequence[PropertyType]):
        self._dotnet_instance.TempProperties = next(_unwrap(None, value))

    @property
    def description(self) -> str:
        return _wrap(self._dotnet_instance.Description)

    @description.setter
    def description(self, value: str):
        self._dotnet_instance.Description = next(_unwrap(None, value))

    @property
    def properties(self) -> Sequence[PropertyType]:
        return _wrap(self._dotnet_instance.Properties)

    @properties.setter
    def properties(self, value: Sequence[PropertyType]):
        self._dotnet_instance.Properties = next(_unwrap(None, value))

    @property
    def errors(self) -> Sequence[ErrorEntry]:
        return _wrap(self._dotnet_instance.Errors)

    @errors.setter
    def errors(self, value: Sequence[ErrorEntry]):
        self._dotnet_instance.Errors = next(_unwrap(None, value))

    @property
    def name(self) -> str:
        return _wrap(self._dotnet_instance.Name)

    @name.setter
    def name(self, value: str):
        self._dotnet_instance.Name = next(_unwrap(None, value))

    @property
    def type_guid(self) -> str:
        return _wrap(self._dotnet_instance.TypeGUID)

    @type_guid.setter
    def type_guid(self, value: str):
        self._dotnet_instance.TypeGUID = next(_unwrap(None, value))

    @property
    def identifier(self) -> System.Guid:
        return _wrap(self._dotnet_instance.Identifier)

    @identifier.setter
    def identifier(self, value: System.Guid):
        self._dotnet_instance.Identifier = next(_unwrap(None, value))

    @overload
    def add_error(self, key: str, is_error: bool, err_code: int, message: str):
        ...

    def add_error(self, *args):
        return _wrap(self._dotnet_instance.AddError(*_unwrap(None, *args)))

    @overload
    def remove_error(self, key: str):
        ...

    def remove_error(self, *args):
        return _wrap(self._dotnet_instance.RemoveError(*_unwrap(None, *args)))

    @overload
    def remove_all_error(self):
        ...

    def remove_all_error(self, *args):
        return _wrap(self._dotnet_instance.RemoveAllError(*_unwrap(None, *args)))

    @overload
    def duplicate_public_errors(self, other_node: BaseNodeType):
        ...

    def duplicate_public_errors(self, *args):
        return _wrap(self._dotnet_instance.DuplicatePublicErrors(*_unwrap(None, *args)))

    @overload
    def get_all_errors(self) -> Sequence[ErrorEntry]:
        ...

    def get_all_errors(self, *args):
        return _wrap(self._dotnet_instance.getAllErrors(*_unwrap(None, *args)))

    @overload
    def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs):
        ...

    def on_collection_changed(self, *args):
        return _wrap(self._dotnet_instance.OnCollectionChanged(*_unwrap(None, *args)))

    @overload
    def compare_to(self, obj: Any) -> int:
        ...

    @overload
    def compare_to(self, other: BaseNodeType) -> int:
        ...

    def compare_to(self, *args):
        return _wrap(self._dotnet_instance.CompareTo(*_unwrap(None, *args)))

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        return _wrap(self._dotnet_instance.ToString(*_unwrap(None, *args)))

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        return _wrap(self._dotnet_instance.Dispose(*_unwrap(None, *args)))

    @overload
    def get_node_type(self) -> NodeType:
        ...

    def get_node_type(self, *args):
        return _wrap(self._dotnet_instance.GetNodeType(*_unwrap(None, *args)))

    @overload
    def get_node_children(self, deep: bool, mode: TraversalMode) -> Sequence[BaseNodeType]:
        ...

    def get_node_children(self, *args):
        return _wrap(self._dotnet_instance.GetNodeChildren(*_unwrap(None, *args)))

    @overload
    def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str]) -> Sequence[BaseNodeType]:
        ...

    @overload
    def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str], leaf_filter: ITraverseNodeFilter, branch_filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]:
        ...

    def get_sorted_node_children(self, *args):
        return _wrap(self._dotnet_instance.GetSortedNodeChildren(*_unwrap(None, *args)))

    @overload
    def find_node_in_array(self, list: Sequence[BaseNodeType]) -> int:
        ...

    def find_node_in_array(self, *args):
        return _wrap(self._dotnet_instance.FindNodeInArray(*_unwrap(None, *args)))

    @overload
    def filter_base_node_types(self, list: Sequence[BaseNodeType], filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]:
        ...

    def filter_base_node_types(self, *args):
        return _wrap(self._dotnet_instance.FilterBaseNodeTypes(*_unwrap(None, *args)))

    @overload
    def is_reference_same_object(self, node_to_compare: BaseNodeType) -> bool:
        ...

    def is_reference_same_object(self, *args):
        return _wrap(self._dotnet_instance.IsReferenceSameObject(*_unwrap(None, *args)))

    @overload
    def rename_node(self, new_name: str) -> bool:
        ...

    def rename_node(self, *args):
        return _wrap(self._dotnet_instance.RenameNode(*_unwrap(None, *args)))

    @overload
    def is_node_relative(self, node_to_check: BaseNodeType) -> bool:
        ...

    def is_node_relative(self, *args):
        return _wrap(self._dotnet_instance.IsNodeRelative(*_unwrap(None, *args)))

    @overload
    def accept(self, visitor: IVisitor):
        ...

    @overload
    def accept(self, visitor_inspection: IVisitorWithInspection) -> IInspectorResult:
        ...

    def accept(self, *args):
        return _wrap(self._dotnet_instance.Accept(*_unwrap(None, *args)))

    @overload
    def get_node_root(self) -> RootType:
        ...

    def get_node_root(self, *args):
        return _wrap(self._dotnet_instance.GetNodeRoot(*_unwrap(None, *args)))

    @overload
    def get_parent(self) -> Tuple[bool, BaseNodeType]:
        ...

    def get_parent(self, *args):
        return _wrap(self._dotnet_instance.GetParent(*_unwrap(None, *args)))

    @overload
    def get_duplicate_reference(self) -> BaseNodeType:
        ...

    def get_duplicate_reference(self, *args):
        return _wrap(self._dotnet_instance.GetDuplicateReference(*_unwrap(None, *args)))

    @overload
    def find_node(self, id: int) -> Tuple[bool, BaseNodeType]:
        ...

    @overload
    def find_node(self, path: Sequence[str]) -> Tuple[bool, BaseNodeType]:
        ...

    def find_node(self, *args):
        return _wrap(self._dotnet_instance.FindNode(*_unwrap(None, *args)))

    @overload
    def find_first_child_node_with_name(self, name: str) -> Tuple[bool, BaseNodeType]:
        ...

    def find_first_child_node_with_name(self, *args):
        return _wrap(self._dotnet_instance.FindFirstChildNodeWithName(*_unwrap(None, *args)))

    @overload
    def find_node_match_guid(self, guid: str, recurse: bool) -> Sequence[BaseNodeType]:
        ...

    @overload
    def find_node_match_guid(self, guid: str) -> BaseNodeType:
        ...

    @overload
    def find_node_match_guid(self, guids: Sequence[str], recurse: bool) -> Tuple[Sequence[BaseNodeType], str]:
        ...

    def find_node_match_guid(self, *args):
        return _wrap(self._dotnet_instance.FindNodeMatchGUID(*_unwrap(None, *args)))

    @overload
    def find_nodesby_guid(self, guids: Sequence[str], recurse: bool, traversal_mode: TraversalMode) -> Tuple[bool, Sequence[BaseNodeType]]:
        ...

    def find_nodesby_guid(self, *args):
        return _wrap(self._dotnet_instance.FindNodesbyGUID(*_unwrap(None, *args)))

    @overload
    def find_guid_up(self, guid: str) -> Tuple[bool, BaseNodeType]:
        ...

    @overload
    def find_guid_up(self, guid: Sequence[str]) -> Tuple[bool, BaseNodeType, str]:
        ...

    def find_guid_up(self, *args):
        return _wrap(self._dotnet_instance.FindGUIDUp(*_unwrap(None, *args)))

    @overload
    def remove_node(self):
        ...

    @overload
    def remove_node(self, for_reuse: bool):
        ...

    def remove_node(self, *args):
        return _wrap(self._dotnet_instance.RemoveNode(*_unwrap(None, *args)))

    @overload
    def move_node_to(self, new_parent: BaseNodeType) -> bool:
        ...

    def move_node_to(self, *args):
        return _wrap(self._dotnet_instance.MoveNodeTo(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def attached_child_node(self, node_to_attached: BaseNodeType) -> bool:
        ...

    def attached_child_node(self, *args):
        return _wrap(self._dotnet_instance.AttachedChildNode(*_unwrap(None, *args)))

    @overload
    def get_node_properties(self) -> Tuple[Sequence[str], Sequence[PropertyContent]]:
        ...

    def get_node_properties(self, *args):
        return _wrap(self._dotnet_instance.GetNodeProperties(*_unwrap(None, *args)))

    @overload
    def get_node_property_type(self, name: str) -> Tuple[bool, PropertyContent]:
        ...

    def get_node_property_type(self, *args):
        return _wrap(self._dotnet_instance.GetNodePropertyType(*_unwrap(None, *args)))

    @overload
    def get_all_properties_with_type(self, prop_type: PropertyContent) -> Sequence[str]:
        ...

    def get_all_properties_with_type(self, *args):
        return _wrap(self._dotnet_instance.GetAllPropertiesWithType(*_unwrap(None, *args)))

    @overload
    def has_node_property(self, name: str) -> Tuple[bool, PropertyContent]:
        ...

    def has_node_property(self, *args):
        return _wrap(self._dotnet_instance.HasNodeProperty(*_unwrap(None, *args)))

    @overload
    def clear_properties(self):
        ...

    def clear_properties(self, *args):
        return _wrap(self._dotnet_instance.ClearProperties(*_unwrap(None, *args)))

    @overload
    def duplicate_properties(self, other_node: BaseNodeType):
        ...

    def duplicate_properties(self, *args):
        return _wrap(self._dotnet_instance.DuplicateProperties(*_unwrap(None, *args)))

    @overload
    def set_string_property(self, name: str, value: str) -> bool:
        ...

    def set_string_property(self, *args):
        return _wrap(self._dotnet_instance.SetStringProperty(*_unwrap(None, *args)))

    @overload
    def set_binary_string_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_binary_string_property(self, *args):
        return _wrap(self._dotnet_instance.SetBinaryStringProperty(*_unwrap(None, *args)))

    @overload
    def set_boolean_property(self, name: str, value: bool) -> bool:
        ...

    def set_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.SetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def set_i32_property(self, name: str, value: int) -> bool:
        ...

    def set_i32_property(self, *args):
        return _wrap(self._dotnet_instance.SetI32Property(*_unwrap(None, *args)))

    @overload
    def set_i16_property(self, name: str, value: int) -> bool:
        ...

    def set_i16_property(self, *args):
        return _wrap(self._dotnet_instance.SetI16Property(*_unwrap(None, *args)))

    @overload
    def set_i64_property(self, name: str, value: int) -> bool:
        ...

    def set_i64_property(self, *args):
        return _wrap(self._dotnet_instance.SetI64Property(*_unwrap(None, *args)))

    @overload
    def set_u32_property(self, name: str, value: int) -> bool:
        ...

    def set_u32_property(self, *args):
        return _wrap(self._dotnet_instance.SetU32Property(*_unwrap(None, *args)))

    @overload
    def set_u16_property(self, name: str, value: int) -> bool:
        ...

    def set_u16_property(self, *args):
        return _wrap(self._dotnet_instance.SetU16Property(*_unwrap(None, *args)))

    @overload
    def set_double_property(self, name: str, value: float) -> bool:
        ...

    def set_double_property(self, *args):
        return _wrap(self._dotnet_instance.SetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def set_u64_property(self, name: str, value: int) -> bool:
        ...

    def set_u64_property(self, *args):
        return _wrap(self._dotnet_instance.SetU64Property(*_unwrap(None, *args)))

    @overload
    def set_variant_property(self, name: str, type: Sequence[int], data: Sequence[int]) -> bool:
        ...

    def set_variant_property(self, *args):
        return _wrap(self._dotnet_instance.SetVariantProperty(*_unwrap(None, *args)))

    @overload
    def set_double_array_property(self, name: str, data: Sequence[float]) -> bool:
        ...

    def set_double_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetDoubleArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_boolean_array_property(self, name: str, data: Sequence[bool]) -> bool:
        ...

    def set_boolean_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetBooleanArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_u64_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u64_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetU64ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_u32_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u32_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetU32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_u16_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u16_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetU16ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_i64_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i64_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetI64ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_i32_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i32_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetI32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_i16_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i16_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetI16ArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_string_array_property(self, name: str, data: Sequence[str]) -> bool:
        ...

    def set_string_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetStringArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_dictionary_property(self, name: str, data: DictionaryProperty) -> bool:
        ...

    def set_dictionary_property(self, *args):
        return _wrap(self._dotnet_instance.SetDictionaryProperty(*_unwrap(None, *args)))

    @overload
    def set_dictionary_array_property(self, name: str, data: Sequence[DictionaryProperty]) -> bool:
        ...

    def set_dictionary_array_property(self, *args):
        return _wrap(self._dotnet_instance.SetDictionaryArrayProperty(*_unwrap(None, *args)))

    @overload
    def set_dependent_file_value(self, name: str, file_path: str, type: DependentFilePropertyType, version: str, force_download: bool, rt_dest: str, supported_target: str, md5: str) -> bool:
        ...

    def set_dependent_file_value(self, *args):
        return _wrap(self._dotnet_instance.SetDependentFileValue(*_unwrap(None, *args)))

    @overload
    def set_dependent_node_value(self, name: str, node: BaseNodeType) -> bool:
        ...

    @overload
    def set_dependent_node_value(self, name: str, node_path: str) -> bool:
        ...

    def set_dependent_node_value(self, *args):
        return _wrap(self._dotnet_instance.SetDependentNodeValue(*_unwrap(None, *args)))

    @overload
    def set_data_source_value(self, name: str, node: BaseNodeType) -> bool:
        ...

    @overload
    def set_data_source_value(self, name: str, node_path: str) -> bool:
        ...

    def set_data_source_value(self, *args):
        return _wrap(self._dotnet_instance.SetDataSourceValue(*_unwrap(None, *args)))

    @overload
    def get_string_property(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string_property(self, *args):
        return _wrap(self._dotnet_instance.GetStringProperty(*_unwrap(None, *args)))

    @overload
    def get_binary_string_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_binary_string_property(self, *args):
        return _wrap(self._dotnet_instance.GetBinaryStringProperty(*_unwrap(None, *args)))

    @overload
    def get_boolean_property(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_boolean_property(self, *args):
        return _wrap(self._dotnet_instance.GetBooleanProperty(*_unwrap(None, *args)))

    @overload
    def get_i32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32_property(self, *args):
        return _wrap(self._dotnet_instance.GetI32Property(*_unwrap(None, *args)))

    @overload
    def get_i16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16_property(self, *args):
        return _wrap(self._dotnet_instance.GetI16Property(*_unwrap(None, *args)))

    @overload
    def get_i64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64_property(self, *args):
        return _wrap(self._dotnet_instance.GetI64Property(*_unwrap(None, *args)))

    @overload
    def get_u32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32_property(self, *args):
        return _wrap(self._dotnet_instance.GetU32Property(*_unwrap(None, *args)))

    @overload
    def get_u16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16_property(self, *args):
        return _wrap(self._dotnet_instance.GetU16Property(*_unwrap(None, *args)))

    @overload
    def get_double_property(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double_property(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleProperty(*_unwrap(None, *args)))

    @overload
    def get_u64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64_property(self, *args):
        return _wrap(self._dotnet_instance.GetU64Property(*_unwrap(None, *args)))

    @overload
    def get_variant_value(self, name: str) -> Tuple[bool, Sequence[int], Sequence[int]]:
        ...

    def get_variant_value(self, *args):
        return _wrap(self._dotnet_instance.GetVariantValue(*_unwrap(None, *args)))

    @overload
    def get_double_array_property(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_double_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetDoubleArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_boolean_array_property(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_boolean_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetBooleanArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_u64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u64_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetU64ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_u32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u32_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetU32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_u16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u16_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetU16ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_i64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i64_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetI64ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_i32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i32_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetI32ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_i16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i16_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetI16ArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_string_array_property(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_string_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetStringArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_dictionary_property(self, name: str) -> Tuple[bool, DictionaryProperty]:
        ...

    def get_dictionary_property(self, *args):
        return _wrap(self._dotnet_instance.GetDictionaryProperty(*_unwrap(None, *args)))

    @overload
    def get_dictionary_array_property(self, name: str) -> Tuple[bool, Sequence[DictionaryProperty]]:
        ...

    def get_dictionary_array_property(self, *args):
        return _wrap(self._dotnet_instance.GetDictionaryArrayProperty(*_unwrap(None, *args)))

    @overload
    def get_dependent_node_value_str(self, name: str) -> Tuple[bool, str]:
        ...

    def get_dependent_node_value_str(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDependentNodeValue(System.String, System.String ByRef)':
                params_tuple = tuple(_unwrap({None: (1, "")}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((result, params_array[1]))

    @overload
    def get_dependent_node_value_basenodetype(self, name: str) -> Tuple[bool, BaseNodeType]:
        ...

    def get_dependent_node_value_basenodetype(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDependentNodeValue(System.String, NationalInstruments.VeriStand.SystemStorage.BaseNodeType ByRef)':
                params_tuple = tuple(_unwrap({None: (1, None)}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((result, params_array[1]))

    @overload
    def get_data_source_node_value_str(self, name: str) -> Tuple[bool, str]:
        ...

    def get_data_source_node_value_str(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDataSourceNodeValue(System.String, System.String ByRef)':
                params_tuple = tuple(_unwrap({None: (1, "")}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((result, params_array[1]))

    @overload
    def get_data_source_node_value_basenodetype(self, name: str) -> Tuple[bool, BaseNodeType]:
        ...

    def get_data_source_node_value_basenodetype(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDataSourceNodeValue(System.String, NationalInstruments.VeriStand.SystemStorage.BaseNodeType ByRef)':
                params_tuple = tuple(_unwrap({None: (1, None)}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((result, params_array[1]))

    @overload
    def get_dependent_file_value(self, name: str) -> Tuple[bool, str, DependentFilePropertyType, str, bool, str, str, str]:
        ...

    def get_dependent_file_value(self, *args):
        return _wrap(self._dotnet_instance.GetDependentFileValue(*_unwrap(None, *args)))

    @overload
    def remove_property(self, name: str) -> bool:
        ...

    def remove_property(self, *args):
        return _wrap(self._dotnet_instance.RemoveProperty(*_unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)))

    @overload
    def clone(self) -> BaseNodeType:
        ...

    def clone(self, *args):
        return _wrap(self._dotnet_instance.Clone(*_unwrap(None, *args)))

    @overload
    def shallow_copy(self) -> BaseNodeType:
        ...

    def shallow_copy(self, *args):
        return _wrap(self._dotnet_instance.ShallowCopy(*_unwrap(None, *args)))

    @overload
    def deep_copy(self) -> BaseNodeType:
        ...

    def deep_copy(self, *args):
        return _wrap(self._dotnet_instance.DeepCopy(*_unwrap(None, *args)))

    @overload
    def start_monitoring_dependent(self, dependent: BaseNodeType, id: str):
        ...

    def start_monitoring_dependent(self, *args):
        return _wrap(self._dotnet_instance.startMonitoringDependent(*_unwrap(None, *args)))

    @overload
    def stop_monitoring_dependent(self, dependent: BaseNodeType, id: str):
        ...

    def stop_monitoring_dependent(self, *args):
        return _wrap(self._dotnet_instance.stopMonitoringDependent(*_unwrap(None, *args)))

    @overload
    def get_observing_nodes(self) -> Iterable[BaseNodeType]:
        ...

    def get_observing_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetObservingNodes(*_unwrap(None, *args)))

    @overload
    def notify_observing_nodes(self, arg: OnNodeChangeEventArgs):
        ...

    def notify_observing_nodes(self, *args):
        return _wrap(self._dotnet_instance.notifyObservingNodes(*_unwrap(None, *args)))

    @overload
    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def get_enumerator(self, *args):
        return _wrap(self._dotnet_instance.GetEnumerator(*_unwrap(None, *args)))

    def _custom_repr(self) -> str:
        return f"(node_path={self.node_path}, name={self.name})"


class PropertyContent(_DotNetEnum):
    """Type of specialized item that can be contained inside a single propertytype."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.PropertyContent:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for PropertyContent")

    @_staticproperty
    def K_STRING() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_STRING"), "K_STRING")

    @_staticproperty
    def K_BOOL() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BOOL"), "K_BOOL")

    @_staticproperty
    def K_I32() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I32"), "K_I32")

    @_staticproperty
    def K_U32() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U32"), "K_U32")

    @_staticproperty
    def K_DOUBLE() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DOUBLE"), "K_DOUBLE")

    @_staticproperty
    def K_U64() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U64"), "K_U64")

    @_staticproperty
    def K_VARIANT() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_VARIANT"), "K_VARIANT")

    @_staticproperty
    def K_DEPENDENTFILE() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DEPENDENTFILE"), "K_DEPENDENTFILE")

    @_staticproperty
    def K_DEPENDENTNODE() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DEPENDENTNODE"), "K_DEPENDENTNODE")

    @_staticproperty
    def K_DATASOURCENODE() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DATASOURCENODE"), "K_DATASOURCENODE")

    @_staticproperty
    def K_U16() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U16"), "K_U16")

    @_staticproperty
    def K_DBLARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DBLARR"), "K_DBLARR")

    @_staticproperty
    def K_U32_ARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U32ARR"), "K_U32_ARR")

    @_staticproperty
    def K_I32_ARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I32ARR"), "K_I32_ARR")

    @_staticproperty
    def K_STRINGARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_STRINGARR"), "K_STRINGARR")

    @_staticproperty
    def K_DICTIONARY() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DICTIONARY"), "K_DICTIONARY")

    @_staticproperty
    def K_DICTIONARYARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DICTIONARYARR"), "K_DICTIONARYARR")

    @_staticproperty
    def K_BINARYSTRING() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BINARYSTRING"), "K_BINARYSTRING")

    @_staticproperty
    def K_I16() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I16"), "K_I16")

    @_staticproperty
    def K_I64() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I64"), "K_I64")

    @_staticproperty
    def K_BOOLARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BOOLARR"), "K_BOOLARR")

    @_staticproperty
    def K_U64_ARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U64ARR"), "K_U64_ARR")

    @_staticproperty
    def K_U16_ARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U16ARR"), "K_U16_ARR")

    @_staticproperty
    def K_I64_ARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I64ARR"), "K_I64_ARR")

    @_staticproperty
    def K_I16_ARR() -> PropertyContent:
        return PropertyContent(getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I16ARR"), "K_I16_ARR")


class WaveformTypeDataType(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for WaveformTypeDataType")

    @_staticproperty
    def DOUBLE() -> WaveformTypeDataType:
        return WaveformTypeDataType(getattr(NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType, "Double"), "DOUBLE")

    @_staticproperty
    def COMPLEX_DOUBLE() -> WaveformTypeDataType:
        return WaveformTypeDataType(getattr(NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType, "ComplexDouble"), "COMPLEX_DOUBLE")


class DocumentType(_DotNetBase):
    """Document class that handle serializing the document."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, filepath: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DocumentType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DocumentType(*_unwrap(None, *args))

    @property
    def no_namespace_schema_location(self) -> str:
        return _wrap(self._dotnet_instance.noNamespaceSchemaLocation)

    @no_namespace_schema_location.setter
    def no_namespace_schema_location(self, value: str):
        self._dotnet_instance.noNamespaceSchemaLocation = next(_unwrap(None, value))

    @_staticproperty
    def project_version() -> Tuple[int, int, int, int]:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.DocumentType.ProjectVersion)

    @_staticproperty
    def schema_uri() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.DocumentType.SchemaUri)

    @property
    def storage_watcher(self) -> SystemStorageWatcher:
        return _wrap(self._dotnet_instance.StorageWatcher)

    @property
    def document_file_path(self) -> str:
        """Access the document file path."""
        return _wrap(self._dotnet_instance.DocumentFilePath)

    @document_file_path.setter
    def document_file_path(self, value: str):
        """Access the document file path."""
        self._dotnet_instance.DocumentFilePath = next(_unwrap(None, value))

    @property
    def md5_checksum(self) -> str:
        return _wrap(self._dotnet_instance.MD5Checksum)

    @md5_checksum.setter
    def md5_checksum(self, value: str):
        self._dotnet_instance.MD5Checksum = next(_unwrap(None, value))

    @property
    def version(self) -> VersionType:
        return _wrap(self._dotnet_instance.Version)

    @version.setter
    def version(self, value: VersionType):
        self._dotnet_instance.Version = next(_unwrap(None, value))

    @property
    def content(self) -> DocumentTypeContent:
        return _wrap(self._dotnet_instance.Content)

    @content.setter
    def content(self, value: DocumentTypeContent):
        self._dotnet_instance.Content = next(_unwrap(None, value))

    @property
    def item(self) -> BaseNodeType:
        return _wrap(self._dotnet_instance.Item)

    @item.setter
    def item(self, value: BaseNodeType):
        self._dotnet_instance.Item = next(_unwrap(None, value))

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        return _wrap(self._dotnet_instance.Dispose(*_unwrap(None, *args)))

    @overload
    def save_system_storage_file(self) -> Tuple[bool, str]:
        ...

    @overload
    def save_system_storage_file(self, filepath: str) -> Tuple[bool, str]:
        ...

    def save_system_storage_file(self, *args):
        return _wrap(self._dotnet_instance.SaveSystemStorageFile(*_unwrap(None, *args)))

    @overload
    def load_system_storage_file(self, filepath: str, schemapath: str) -> Tuple[bool, str]:
        ...

    @overload
    def load_system_storage_file(self, filepath: str, schemapath: str, version_to_mutate: Sequence[XMLVersionInfo], xslst_file_paths: Sequence[str]) -> Tuple[bool, str]:
        ...

    def load_system_storage_file(self, *args):
        return _wrap(self._dotnet_instance.LoadSystemStorageFile(*_unwrap(None, *args)))

    @overload
    def load_project_xml_file(self, filepath: str) -> Tuple[bool, str, bool]:
        ...

    def load_project_xml_file(self, *args):
        return _wrap(self._dotnet_instance.LoadProjectXMLFile(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def get_system_definition_file_path(project_file_path: str) -> str:
        ...

    def get_system_definition_file_path(*args):
        return _wrap(NationalInstruments.VeriStand.SystemStorage.DocumentType.GetSystemDefinitionFilePath(*_unwrap(None, *args)))

    @overload
    def set_content(self, node: BaseNodeType):
        ...

    def set_content(self, *args):
        return _wrap(self._dotnet_instance.SetContent(*_unwrap(None, *args)))

    @overload
    def get_duplicate_reference(self) -> DocumentType:
        ...

    def get_duplicate_reference(self, *args):
        return _wrap(self._dotnet_instance.GetDuplicateReference(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def read_version_info(version_tag: str, file_path: str) -> XMLVersionInfo:
        ...

    def read_version_info(*args):
        return _wrap(NationalInstruments.VeriStand.SystemStorage.DocumentType.ReadVersionInfo(*_unwrap(None, *args)))


class VersionType(_DotNetBase):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.VersionType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.VersionType(*_unwrap(None, *args))

    @property
    def major(self) -> int:
        return _wrap(self._dotnet_instance.Major)

    @major.setter
    def major(self, value: int):
        self._dotnet_instance.Major = next(_unwrap(None, value))

    @property
    def minor(self) -> int:
        return _wrap(self._dotnet_instance.Minor)

    @minor.setter
    def minor(self, value: int):
        self._dotnet_instance.Minor = next(_unwrap(None, value))

    @property
    def fix(self) -> int:
        return _wrap(self._dotnet_instance.Fix)

    @fix.setter
    def fix(self, value: int):
        self._dotnet_instance.Fix = next(_unwrap(None, value))

    @property
    def build(self) -> int:
        return _wrap(self._dotnet_instance.Build)

    @build.setter
    def build(self, value: int):
        self._dotnet_instance.Build = next(_unwrap(None, value))


class DependentFilePropertyType(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DependentFilePropertyType")

    @_staticproperty
    def ABSOLUTE() -> DependentFilePropertyType:
        return DependentFilePropertyType(getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "Absolute"), "ABSOLUTE")

    @_staticproperty
    def RELATIVE() -> DependentFilePropertyType:
        return DependentFilePropertyType(getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "Relative"), "RELATIVE")

    @_staticproperty
    def TO_COMMON_DOC_DIR() -> DependentFilePropertyType:
        return DependentFilePropertyType(getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "ToCommonDocDir"), "TO_COMMON_DOC_DIR")

    @_staticproperty
    def TO_APPLICATION_DATA_DIR() -> DependentFilePropertyType:
        return DependentFilePropertyType(getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "ToApplicationDataDir"), "TO_APPLICATION_DATA_DIR")


class ErrorEntry(_DotNetBase):
    """ErrorEntry represent an error on the basenodetype."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, key: str, is_error: bool, code: int, msg: str):
        ...

    @overload
    def __init__(self, to_copy: ErrorEntry):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ErrorEntry:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ErrorEntry(*_unwrap(None, *args))

    @property
    def message(self) -> str:
        return _wrap(self._dotnet_instance.Message)

    @message.setter
    def message(self, value: str):
        self._dotnet_instance.Message = next(_unwrap(None, value))

    @property
    def key(self) -> str:
        return _wrap(self._dotnet_instance.Key)

    @key.setter
    def key(self, value: str):
        self._dotnet_instance.Key = next(_unwrap(None, value))

    @property
    def is_error(self) -> bool:
        return _wrap(self._dotnet_instance.IsError)

    @is_error.setter
    def is_error(self, value: bool):
        self._dotnet_instance.IsError = next(_unwrap(None, value))

    @property
    def code(self) -> int:
        return _wrap(self._dotnet_instance.Code)

    @code.setter
    def code(self, value: int):
        self._dotnet_instance.Code = next(_unwrap(None, value))

    @overload
    def clone(self) -> ErrorEntry:
        ...

    def clone(self, *args):
        return _wrap(self._dotnet_instance.Clone(*_unwrap(None, *args)))

    @overload
    def equals(self, other: ErrorEntry) -> bool:
        ...

    @overload
    def equals(self, obj: Any) -> bool:
        ...

    def equals(self, *args):
        return _wrap(self._dotnet_instance.Equals(*_unwrap(None, *args)))

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_hash_code(self, *args):
        return _wrap(self._dotnet_instance.GetHashCode(*_unwrap(None, *args)))


class PropertyType(_DotNetBase):
    """This class represent a single property of a BaseNodeType.
            The class contains a name of the property and the actual property value."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, to_copy: PropertyType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.PropertyType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.PropertyType(*_unwrap(None, *args))

    @property
    def type(self) -> PropertyContent:
        """Akin to reflection method to return the actual property type."""
        return _wrap(self._dotnet_instance.Type)

    @property
    def item(self) -> Any:
        return _wrap(self._dotnet_instance.Item)

    @item.setter
    def item(self, value: Any):
        self._dotnet_instance.Item = next(_unwrap(None, value))

    @property
    def name(self) -> str:
        return _wrap(self._dotnet_instance.Name)

    @name.setter
    def name(self, value: str):
        self._dotnet_instance.Name = next(_unwrap(None, value))

    @overload
    def clone(self) -> PropertyType:
        ...

    def clone(self, *args):
        return _wrap(self._dotnet_instance.Clone(*_unwrap(None, *args)))

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        return _wrap(self._dotnet_instance.Dispose(*_unwrap(None, *args)))

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class NodeType(_DotNetEnum):
    """Type of actual node."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.NodeType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for NodeType")

    @_staticproperty
    def K_BASE() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_BASE"), "K_BASE")

    @_staticproperty
    def K_ALIAS() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_ALIAS"), "K_ALIAS")

    @_staticproperty
    def K_CHANNEL() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_CHANNEL"), "K_CHANNEL")

    @_staticproperty
    def K_SECTION() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_SECTION"), "K_SECTION")

    @_staticproperty
    def K_TARGET() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_TARGET"), "K_TARGET")

    @_staticproperty
    def K_TARGETSECTION() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_TARGETSECTION"), "K_TARGETSECTION")

    @_staticproperty
    def K_ROOT() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_ROOT"), "K_ROOT")

    @_staticproperty
    def K_WAVEFORM() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_WAVEFORM"), "K_WAVEFORM")

    @_staticproperty
    def K_PARAMETER() -> NodeType:
        return NodeType(getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_PARAMETER"), "K_PARAMETER")


class TraversalMode(_DotNetEnum):
    """Type of enumeration that is supported when we are traversing the tree of nodes."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.TraversalMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TraversalMode")

    @_staticproperty
    def K_BFS() -> TraversalMode:
        return TraversalMode(getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_BFS"), "K_BFS")

    @_staticproperty
    def K_DFS() -> TraversalMode:
        return TraversalMode(getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_DFS"), "K_DFS")

    @_staticproperty
    def K_CHILDONLY() -> TraversalMode:
        return TraversalMode(getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_CHILDONLY"), "K_CHILDONLY")

    @_staticproperty
    def K_UP() -> TraversalMode:
        return TraversalMode(getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_UP"), "K_UP")


class ITraverseNodeFilter(_DotNetBase):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ITraverseNodeFilter:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ITraverseNodeFilter")

    @overload
    def check_with_filter(self, node: BaseNodeType) -> bool:
        ...

    def check_with_filter(self, *args):
        return _wrap(self._dotnet_instance.CheckWithFilter(*_unwrap(None, *args)))


class IVisitor(_DotNetBase):
    """For every type element in the tree declare a visit function for it."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.IVisitor:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IVisitor")

    @overload
    def visit(self, element: BaseNodeType):
        ...

    @overload
    def visit(self, element: ChannelType):
        ...

    @overload
    def visit(self, element: SectionType):
        ...

    @overload
    def visit(self, element: AliasType):
        ...

    @overload
    def visit(self, element: ParameterType):
        ...

    @overload
    def visit(self, element: TargetType):
        ...

    @overload
    def visit(self, element: RootType):
        ...

    @overload
    def visit(self, element: TargetSectionsType):
        ...

    def visit(self, *args):
        return _wrap(self._dotnet_instance.Visit(*_unwrap(None, *args)))


class IVisitorWithInspection(_DotNetBase):
    """For every type element in the tree declare a visit function for it.
             This is a variant of the visitor function where we allow an object
             to be returned by the visitor class so the caller can do some post-processing
             based on the object value.
             This allows postwalk operation on the tree."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.IVisitorWithInspection:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IVisitorWithInspection")

    @overload
    def visit(self, element: BaseNodeType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: ChannelType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: SectionType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: AliasType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: ParameterType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: TargetType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: RootType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: TargetSectionsType) -> IInspectorResult:
        ...

    def visit(self, *args):
        return _wrap(self._dotnet_instance.Visit(*_unwrap(None, *args)))


class IInspectorResult(_DotNetBase):
    """The generic return value that the IVisitorWithInspection support."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.IInspectorResult:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IInspectorResult")

    @overload
    def result(self) -> Any:
        ...

    def result(self, *args):
        return _wrap(self._dotnet_instance.Result(*_unwrap(None, *args)))


class RootType(BaseNodeType):
    """Specialized class that denotes a root of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: RootType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.RootType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.RootType(*_unwrap(None, *args))

    @property
    def target_sections(self) -> TargetSectionsType:
        return _wrap(self._dotnet_instance.TargetSections)

    @target_sections.setter
    def target_sections(self, value: TargetSectionsType):
        self._dotnet_instance.TargetSections = next(_unwrap(None, value))

    @property
    def section(self) -> Sequence[SectionType]:
        return _wrap(self._dotnet_instance.Section)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        self._dotnet_instance.Section = next(_unwrap(None, value))

    @overload
    def get_owning_document_file_path(self) -> str:
        ...

    def get_owning_document_file_path(self, *args):
        return _wrap(self._dotnet_instance.GetOwningDocumentFilePath(*_unwrap(None, *args)))

    @overload
    def refresh_node_dependencies(self):
        ...

    def refresh_node_dependencies(self, *args):
        return _wrap(self._dotnet_instance.RefreshNodeDependencies(*_unwrap(None, *args)))

    @overload
    def set_target_section(self, new_target_section: TargetSectionsType) -> bool:
        ...

    @overload
    def set_target_section(self, new_target_section: TargetSectionsType, relink: bool) -> bool:
        ...

    def set_target_section(self, *args):
        return _wrap(self._dotnet_instance.SetTargetSection(*_unwrap(None, *args)))

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleSectionType(*_unwrap(None, *args)))

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderSectionTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetSectionTypeChildNodes(*_unwrap(None, *args)))


class BaseCustomNodeProperty(_DotNetBase):
    """Base Class for Property Type that encapsulate basic data type. This
            allow for the class to automatically register the owning BaseNodeType
            to changes that happened to the encapsulated data type."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, to_copy: BaseCustomNodeProperty):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.BaseCustomNodeProperty:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.BaseCustomNodeProperty(*_unwrap(None, *args))

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        return _wrap(self._dotnet_instance.Dispose(*_unwrap(None, *args)))

    @overload
    def clone(self) -> BaseCustomNodeProperty:
        ...

    def clone(self, *args):
        return _wrap(self._dotnet_instance.Clone(*_unwrap(None, *args)))


class DictionaryProperty(BaseCustomNodeProperty):
    """Dictionary property implementation implement cloneable so we can clone property savely."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, to_copy: DictionaryProperty):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DictionaryProperty:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DictionaryProperty(*_unwrap(None, *args))

    @property
    def count(self) -> int:
        return _wrap(self._dotnet_instance.Count)

    @property
    def elem(self) -> Sequence[DictionaryElement]:
        return _wrap(self._dotnet_instance.Elem)

    @elem.setter
    def elem(self, value: Sequence[DictionaryElement]):
        self._dotnet_instance.Elem = next(_unwrap(None, value))

    @overload
    def clear(self):
        ...

    def clear(self, *args):
        return _wrap(self._dotnet_instance.Clear(*_unwrap(None, *args)))

    @overload
    def remove_element(self, key: str) -> bool:
        ...

    def remove_element(self, *args):
        return _wrap(self._dotnet_instance.RemoveElement(*_unwrap(None, *args)))

    @overload
    def add_string(self, name: str, value: str) -> bool:
        ...

    def add_string(self, *args):
        return _wrap(self._dotnet_instance.AddString(*_unwrap(None, *args)))

    @overload
    def add_boolean(self, name: str, value: bool) -> bool:
        ...

    def add_boolean(self, *args):
        return _wrap(self._dotnet_instance.AddBoolean(*_unwrap(None, *args)))

    @overload
    def add_i32(self, name: str, value: int) -> bool:
        ...

    def add_i32(self, *args):
        return _wrap(self._dotnet_instance.AddI32(*_unwrap(None, *args)))

    @overload
    def add_i16(self, name: str, value: int) -> bool:
        ...

    def add_i16(self, *args):
        return _wrap(self._dotnet_instance.AddI16(*_unwrap(None, *args)))

    @overload
    def add_i64(self, name: str, value: int) -> bool:
        ...

    def add_i64(self, *args):
        return _wrap(self._dotnet_instance.AddI64(*_unwrap(None, *args)))

    @overload
    def add_u32(self, name: str, value: int) -> bool:
        ...

    def add_u32(self, *args):
        return _wrap(self._dotnet_instance.AddU32(*_unwrap(None, *args)))

    @overload
    def add_u16(self, name: str, value: int) -> bool:
        ...

    def add_u16(self, *args):
        return _wrap(self._dotnet_instance.AddU16(*_unwrap(None, *args)))

    @overload
    def add_double(self, name: str, value: float) -> bool:
        ...

    def add_double(self, *args):
        return _wrap(self._dotnet_instance.AddDouble(*_unwrap(None, *args)))

    @overload
    def add_u64(self, name: str, value: int) -> bool:
        ...

    def add_u64(self, *args):
        return _wrap(self._dotnet_instance.AddU64(*_unwrap(None, *args)))

    @overload
    def add_arr_double(self, name: str, value: Sequence[float]) -> bool:
        ...

    def add_arr_double(self, *args):
        return _wrap(self._dotnet_instance.AddArrDouble(*_unwrap(None, *args)))

    @overload
    def add_arr_boolean(self, name: str, value: Sequence[bool]) -> bool:
        ...

    def add_arr_boolean(self, *args):
        return _wrap(self._dotnet_instance.AddArrBoolean(*_unwrap(None, *args)))

    @overload
    def add_arr_u64(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u64(self, *args):
        return _wrap(self._dotnet_instance.AddArrU64(*_unwrap(None, *args)))

    @overload
    def add_arr_u32(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u32(self, *args):
        return _wrap(self._dotnet_instance.AddArrU32(*_unwrap(None, *args)))

    @overload
    def add_arr_u16(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u16(self, *args):
        return _wrap(self._dotnet_instance.AddArrU16(*_unwrap(None, *args)))

    @overload
    def add_arr_i64(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i64(self, *args):
        return _wrap(self._dotnet_instance.AddArrI64(*_unwrap(None, *args)))

    @overload
    def add_arr_i32(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i32(self, *args):
        return _wrap(self._dotnet_instance.AddArrI32(*_unwrap(None, *args)))

    @overload
    def add_arr_i16(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i16(self, *args):
        return _wrap(self._dotnet_instance.AddArrI16(*_unwrap(None, *args)))

    @overload
    def add_arr_string(self, name: str, value: Sequence[str]) -> bool:
        ...

    def add_arr_string(self, *args):
        return _wrap(self._dotnet_instance.AddArrString(*_unwrap(None, *args)))

    @overload
    def get_string(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string(self, *args):
        return _wrap(self._dotnet_instance.GetString(*_unwrap(None, *args)))

    @overload
    def get_bool(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_bool(self, *args):
        return _wrap(self._dotnet_instance.GetBool(*_unwrap(None, *args)))

    @overload
    def get_i32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32(self, *args):
        return _wrap(self._dotnet_instance.GetI32(*_unwrap(None, *args)))

    @overload
    def get_i16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16(self, *args):
        return _wrap(self._dotnet_instance.GetI16(*_unwrap(None, *args)))

    @overload
    def get_i64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64(self, *args):
        return _wrap(self._dotnet_instance.GetI64(*_unwrap(None, *args)))

    @overload
    def get_u32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32(self, *args):
        return _wrap(self._dotnet_instance.GetU32(*_unwrap(None, *args)))

    @overload
    def get_u16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16(self, *args):
        return _wrap(self._dotnet_instance.GetU16(*_unwrap(None, *args)))

    @overload
    def get_double(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double(self, *args):
        return _wrap(self._dotnet_instance.GetDouble(*_unwrap(None, *args)))

    @overload
    def get_u64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64(self, *args):
        return _wrap(self._dotnet_instance.GetU64(*_unwrap(None, *args)))

    @overload
    def get_arr_double(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_arr_double(self, *args):
        return _wrap(self._dotnet_instance.GetArrDouble(*_unwrap(None, *args)))

    @overload
    def get_arr_boolean(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_arr_boolean(self, *args):
        return _wrap(self._dotnet_instance.GetArrBoolean(*_unwrap(None, *args)))

    @overload
    def get_arr_u64(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u64(self, *args):
        return _wrap(self._dotnet_instance.GetArrU64(*_unwrap(None, *args)))

    @overload
    def get_arr_u32(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u32(self, *args):
        return _wrap(self._dotnet_instance.GetArrU32(*_unwrap(None, *args)))

    @overload
    def get_arr_u16(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u16(self, *args):
        return _wrap(self._dotnet_instance.GetArrU16(*_unwrap(None, *args)))

    @overload
    def get_arr_i64(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i64(self, *args):
        return _wrap(self._dotnet_instance.GetArrI64(*_unwrap(None, *args)))

    @overload
    def get_arr_i32(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i32(self, *args):
        return _wrap(self._dotnet_instance.GetArrI32(*_unwrap(None, *args)))

    @overload
    def get_arr_i16(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i16(self, *args):
        return _wrap(self._dotnet_instance.GetArrI16(*_unwrap(None, *args)))

    @overload
    def get_arr_string(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_arr_string(self, *args):
        return _wrap(self._dotnet_instance.GetArrString(*_unwrap(None, *args)))


class OnNodeChangeEventArgs(_DotNetBase):
    """Event data that get send when the node change argument is fired."""

    @overload
    def __init__(self, action: str, data: Sequence[int]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs(*_unwrap(None, *args))

    @_staticproperty
    def k_deleted() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_DELETED)

    @_staticproperty
    def k_error() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_ERROR)

    @_staticproperty
    def k_no_error() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_NO_ERROR)

    @_staticproperty
    def k_property_changed() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_PROPERTY_CHANGED)

    @_staticproperty
    def k_collection_changed() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_COLLECTION_CHANGED)

    @property
    def m_action(self) -> str:
        """public field to access the action"""
        return _wrap(self._dotnet_instance.m_action)

    @property
    def m_data(self) -> Sequence[int]:
        """public field to access the generic data field."""
        return _wrap(self._dotnet_instance.m_data)


class ChannelType(BaseNodeType):
    """Specialized class to denote the channel type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: ChannelType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ChannelType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ChannelType(*_unwrap(None, *args))

    @property
    def is_readable(self) -> bool:
        """field to indicate if channel is readable"""
        return _wrap(self._dotnet_instance.IsReadable)

    @property
    def is_writable(self) -> bool:
        """field to indicate if channel is writable"""
        return _wrap(self._dotnet_instance.IsWritable)

    @property
    def is_faultable(self) -> bool:
        """field to indicate if channel is faultable"""
        return _wrap(self._dotnet_instance.IsFaultable)

    @property
    def is_scalable(self) -> bool:
        """field to indicate if channel is scalable"""
        return _wrap(self._dotnet_instance.IsScalable)

    @property
    def data_length(self) -> int:
        """return the data length of the channel."""
        return _wrap(self._dotnet_instance.DataLength)

    @property
    def default_value(self) -> Sequence[float]:
        return _wrap(self._dotnet_instance.DefaultValue)

    @default_value.setter
    def default_value(self, value: Sequence[float]):
        self._dotnet_instance.DefaultValue = next(_unwrap(None, value))

    @property
    def row_dim(self) -> int:
        return _wrap(self._dotnet_instance.RowDim)

    @row_dim.setter
    def row_dim(self, value: int):
        self._dotnet_instance.RowDim = next(_unwrap(None, value))

    @property
    def col_dim(self) -> int:
        return _wrap(self._dotnet_instance.ColDim)

    @col_dim.setter
    def col_dim(self, value: int):
        self._dotnet_instance.ColDim = next(_unwrap(None, value))

    @property
    def units(self) -> str:
        return _wrap(self._dotnet_instance.Units)

    @units.setter
    def units(self, value: str):
        self._dotnet_instance.Units = next(_unwrap(None, value))

    @property
    def bit_fields(self) -> int:
        return _wrap(self._dotnet_instance.BitFields)

    @bit_fields.setter
    def bit_fields(self, value: int):
        self._dotnet_instance.BitFields = next(_unwrap(None, value))

    @overload
    def is_under_target(self, target_to_check: TargetType) -> bool:
        ...

    def is_under_target(self, *args):
        return _wrap(self._dotnet_instance.IsUnderTarget(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def get_value_table(channel: ChannelType) -> Tuple[bool, Sequence[str], Sequence[float]]:
        ...

    def get_value_table(*args):
        return _wrap(NationalInstruments.VeriStand.SystemStorage.ChannelType.GetValueTable(*_unwrap(None, *args)))

    @staticmethod
    @overload
    def set_value_table(channel: ChannelType, names: Sequence[str], values: Sequence[float]):
        ...

    def set_value_table(*args):
        return _wrap(NationalInstruments.VeriStand.SystemStorage.ChannelType.SetValueTable(*_unwrap(None, *args)))


class SystemStorageWatcher(_DotNetBase):
    """Public class to abstract the actual watcher node internals."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.SystemStorageWatcher:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SystemStorageWatcher")

    @_staticproperty
    def k_system_storage_watcher_dependentid() -> str:
        return _wrap(NationalInstruments.VeriStand.SystemStorage.SystemStorageWatcher.K_SYSTEM_STORAGE_WATCHER_DEPENDENTID)

    @property
    def error_count(self) -> int:
        """Gets the current error count"""
        return _wrap(self._dotnet_instance.ErrorCount)

    @property
    def has_modification(self) -> bool:
        return _wrap(self._dotnet_instance.HasModification)

    @property
    def error_in_system(self) -> Sequence[BaseNodeType]:
        return _wrap(self._dotnet_instance.ErrorInSystem)

    @property
    def has_any_error(self) -> bool:
        return _wrap(self._dotnet_instance.HasAnyError)

    @overload
    def reset_modification_flag(self):
        ...

    def reset_modification_flag(self, *args):
        return _wrap(self._dotnet_instance.ResetModificationFlag(*_unwrap(None, *args)))

    @overload
    def fire_count_event(self):
        ...

    def fire_count_event(self, *args):
        return _wrap(self._dotnet_instance.FireCountEvent(*_unwrap(None, *args)))

    @overload
    def supress_notification(self):
        ...

    def supress_notification(self, *args):
        return _wrap(self._dotnet_instance.SupressNotification(*_unwrap(None, *args)))

    @overload
    def unsupress_notification(self):
        ...

    def unsupress_notification(self, *args):
        return _wrap(self._dotnet_instance.UnsupressNotification(*_unwrap(None, *args)))

    @overload
    def is_node_in_error_collection(self, node: BaseNodeType) -> bool:
        ...

    def is_node_in_error_collection(self, *args):
        return _wrap(self._dotnet_instance.IsNodeInErrorCollection(*_unwrap(None, *args)))

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        return _wrap(self._dotnet_instance.Dispose(*_unwrap(None, *args)))


class DocumentTypeContent(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DocumentTypeContent")

    @_staticproperty
    def DEFINITION() -> DocumentTypeContent:
        return DocumentTypeContent(getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "Definition"), "DEFINITION")

    @_staticproperty
    def EXPORT() -> DocumentTypeContent:
        return DocumentTypeContent(getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "Export"), "EXPORT")

    @_staticproperty
    def SLSC() -> DocumentTypeContent:
        return DocumentTypeContent(getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "SLSC"), "SLSC")


class SectionType(BaseNodeType):
    """Specialized node that implement Section"""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: SectionType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.SectionType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.SectionType(*_unwrap(None, *args))

    @property
    def section(self) -> Sequence[SectionType]:
        return _wrap(self._dotnet_instance.Section)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        self._dotnet_instance.Section = next(_unwrap(None, value))

    @property
    def channel(self) -> Sequence[ChannelType]:
        return _wrap(self._dotnet_instance.Channel)

    @channel.setter
    def channel(self, value: Sequence[ChannelType]):
        self._dotnet_instance.Channel = next(_unwrap(None, value))

    @property
    def alias(self) -> Sequence[AliasType]:
        return _wrap(self._dotnet_instance.Alias)

    @alias.setter
    def alias(self, value: Sequence[AliasType]):
        self._dotnet_instance.Alias = next(_unwrap(None, value))

    @property
    def parameter(self) -> Sequence[ParameterType]:
        return _wrap(self._dotnet_instance.Parameter)

    @parameter.setter
    def parameter(self, value: Sequence[ParameterType]):
        self._dotnet_instance.Parameter = next(_unwrap(None, value))

    @property
    def waveform(self) -> Sequence[WaveformType]:
        return _wrap(self._dotnet_instance.Waveform)

    @waveform.setter
    def waveform(self, value: Sequence[WaveformType]):
        self._dotnet_instance.Waveform = next(_unwrap(None, value))

    @overload
    def attached_child_node_without_check(self, node: BaseNodeType):
        ...

    def attached_child_node_without_check(self, *args):
        return _wrap(self._dotnet_instance.AttachedChildNodeWithoutCheck(*_unwrap(None, *args)))

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleSectionType(*_unwrap(None, *args)))

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderSectionTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetSectionTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def add_multiple_channel_type(self, new_nodes: Sequence[ChannelType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_channel_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleChannelType(*_unwrap(None, *args)))

    @overload
    def reorder_channel_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_channel_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderChannelTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_channel_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_channel_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetChannelTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def add_multiple_alias_type(self, new_nodes: Sequence[AliasType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_alias_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleAliasType(*_unwrap(None, *args)))

    @overload
    def reorder_alias_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_alias_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderAliasTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_alias_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_alias_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetAliasTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def add_multiple_parameter_type(self, new_nodes: Sequence[ParameterType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_parameter_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleParameterType(*_unwrap(None, *args)))

    @overload
    def reorder_parameter_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_parameter_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderParameterTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_parameter_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_parameter_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetParameterTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def add_multiple_waveform_type(self, new_nodes: Sequence[WaveformType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_waveform_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleWaveformType(*_unwrap(None, *args)))

    @overload
    def reorder_waveform_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_waveform_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderWaveformTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_waveform_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_waveform_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetWaveformTypeChildNodes(*_unwrap(None, *args)))


class AliasType(BaseNodeType):
    """Specialized class to denote the alias type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: AliasType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.AliasType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.AliasType(*_unwrap(None, *args))

    @property
    def resolve_alias_reference(self) -> BaseNodeType:
        """Gets the referenced channel."""
        return _wrap(self._dotnet_instance.ResolveAliasReference)


class ParameterType(BaseNodeType):
    """Specialized class to denote the parameter type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: ParameterType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ParameterType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ParameterType(*_unwrap(None, *args))

    @property
    def row_dim(self) -> int:
        return _wrap(self._dotnet_instance.RowDim)

    @row_dim.setter
    def row_dim(self, value: int):
        self._dotnet_instance.RowDim = next(_unwrap(None, value))

    @property
    def col_dim(self) -> int:
        return _wrap(self._dotnet_instance.ColDim)

    @col_dim.setter
    def col_dim(self, value: int):
        self._dotnet_instance.ColDim = next(_unwrap(None, value))


class TargetType(BaseNodeType):
    """Specialized node that implement Target"""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: TargetType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.TargetType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.TargetType(*_unwrap(None, *args))

    @property
    def dfs_object_enumerator(self) -> System.Collections.IEnumerator:
        """Return a non generic Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found."""
        return _wrap(self._dotnet_instance.DFSObjectEnumerator)

    @property
    def section(self) -> Sequence[SectionType]:
        return _wrap(self._dotnet_instance.Section)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        self._dotnet_instance.Section = next(_unwrap(None, value))

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleSectionType(*_unwrap(None, *args)))

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderSectionTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetSectionTypeChildNodes(*_unwrap(None, *args)))


class TargetSectionsType(BaseNodeType):
    """Specialized node that implement TargetSections"""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: TargetSectionsType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.TargetSectionsType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.TargetSectionsType(*_unwrap(None, *args))

    @property
    def target(self) -> Sequence[TargetType]:
        return _wrap(self._dotnet_instance.Target)

    @target.setter
    def target(self, value: Sequence[TargetType]):
        self._dotnet_instance.Target = next(_unwrap(None, value))

    @overload
    def add_multiple_target_type(self, new_nodes: Sequence[TargetType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_target_type(self, *args):
        return _wrap(self._dotnet_instance.AddMultipleTargetType(*_unwrap(None, *args)))

    @overload
    def reorder_target_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_target_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.ReorderTargetTypeChildNodes(*_unwrap(None, *args)))

    @overload
    def get_target_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_target_type_child_nodes(self, *args):
        return _wrap(self._dotnet_instance.GetTargetTypeChildNodes(*_unwrap(None, *args)))


class DuplicateOp(_DotNetEnum):
    """Operations possible when adding nodes and duplicates are found."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DuplicateOp:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DuplicateOp")

    @_staticproperty
    def ASSERT() -> DuplicateOp:
        return DuplicateOp(getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "Assert"), "ASSERT")

    @_staticproperty
    def RENAME() -> DuplicateOp:
        return DuplicateOp(getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "Rename"), "RENAME")

    @_staticproperty
    def UNIQUE_ONLY() -> DuplicateOp:
        return DuplicateOp(getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "UniqueOnly"), "UNIQUE_ONLY")


class DictionaryElement(_DotNetBase):
    """Dictionary Element implementation implement cloneable so we can clone Dictionary Element savely."""

    @overload
    def __init__(self, to_copy: DictionaryElement):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DictionaryElement:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DictionaryElement(*_unwrap(None, *args))

    @property
    def item(self) -> Any:
        return _wrap(self._dotnet_instance.Item)

    @item.setter
    def item(self, value: Any):
        self._dotnet_instance.Item = next(_unwrap(None, value))

    @property
    def key(self) -> str:
        return _wrap(self._dotnet_instance.Key)

    @key.setter
    def key(self, value: str):
        self._dotnet_instance.Key = next(_unwrap(None, value))

    @overload
    def clone(self) -> DictionaryElement:
        ...

    def clone(self, *args):
        return _wrap(self._dotnet_instance.Clone(*_unwrap(None, *args)))


class WaveformType(BaseNodeType):
    """Specialized class to denote the waveform type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str, data_type: WaveformTypeDataType):
        ...

    @overload
    def __init__(self, to_copy: WaveformType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.WaveformType:
            self._dotnet_instance = args[0]
        else:
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.WaveformType(*_unwrap(None, *args))

    @property
    def data_type(self) -> WaveformTypeDataType:
        return _wrap(self._dotnet_instance.DataType)

    @data_type.setter
    def data_type(self, value: WaveformTypeDataType):
        self._dotnet_instance.DataType = next(_unwrap(None, value))

    @property
    def units(self) -> str:
        return _wrap(self._dotnet_instance.Units)

    @units.setter
    def units(self, value: str):
        self._dotnet_instance.Units = next(_unwrap(None, value))
