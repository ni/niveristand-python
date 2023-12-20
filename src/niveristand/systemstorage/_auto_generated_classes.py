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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.BaseNodeType(*unwrapped)

    @property
    def node_path_array(self) -> Sequence[str]:
        """Get the node path of the node as path array."""
        dotnet_result = self._dotnet_instance.NodePathArray
        return _wrap(dotnet_result)

    @property
    def node_path(self) -> str:
        """Get the node path of the node as a string."""
        dotnet_result = self._dotnet_instance.NodePath
        return _wrap(dotnet_result)

    @property
    def errors_array(self) -> Sequence[ErrorEntry]:
        dotnet_result = self._dotnet_instance.ErrorsArray
        return _wrap(dotnet_result)

    @errors_array.setter
    def errors_array(self, value: Sequence[ErrorEntry]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ErrorsArray = next(unwrapped)

    @property
    def bfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return a Breath First Search enumerator. This enumerator iterates through all children of
            then node directly before diving into the hierarchy. For leaf type nodes it will return only itself."""
        dotnet_result = self._dotnet_instance.BFSEnumerator
        return _wrap(dotnet_result)

    @property
    def dfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return a Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found."""
        dotnet_result = self._dotnet_instance.DFSEnumerator
        return _wrap(dotnet_result)

    @property
    def child_only_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return enumerator that allow user to enumerate through the children of this node only."""
        dotnet_result = self._dotnet_instance.ChildOnlyEnumerator
        return _wrap(dotnet_result)

    @property
    def child_only_object_enumerator(self) -> System.Collections.IEnumerator:
        """Return non generic enumerator that allow user to enumerate through the children of this node only."""
        dotnet_result = self._dotnet_instance.ChildOnlyObjectEnumerator
        return _wrap(dotnet_result)

    @property
    def trav_parent_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return enumerator that allow user to enumerate through the parent."""
        dotnet_result = self._dotnet_instance.TravParentEnumerator
        return _wrap(dotnet_result)

    @property
    def id(self) -> int:
        """ID"""
        dotnet_result = self._dotnet_instance.ID
        return _wrap(dotnet_result)

    @id.setter
    def id(self, value: int):
        """ID"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ID = next(unwrapped)

    @property
    def temp_properties(self) -> Sequence[PropertyType]:
        dotnet_result = self._dotnet_instance.TempProperties
        return _wrap(dotnet_result)

    @temp_properties.setter
    def temp_properties(self, value: Sequence[PropertyType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TempProperties = next(unwrapped)

    @property
    def description(self) -> str:
        dotnet_result = self._dotnet_instance.Description
        return _wrap(dotnet_result)

    @description.setter
    def description(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Description = next(unwrapped)

    @property
    def properties(self) -> Sequence[PropertyType]:
        dotnet_result = self._dotnet_instance.Properties
        return _wrap(dotnet_result)

    @properties.setter
    def properties(self, value: Sequence[PropertyType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Properties = next(unwrapped)

    @property
    def errors(self) -> Sequence[ErrorEntry]:
        dotnet_result = self._dotnet_instance.Errors
        return _wrap(dotnet_result)

    @errors.setter
    def errors(self, value: Sequence[ErrorEntry]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Errors = next(unwrapped)

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @name.setter
    def name(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Name = next(unwrapped)

    @property
    def type_guid(self) -> str:
        dotnet_result = self._dotnet_instance.TypeGUID
        return _wrap(dotnet_result)

    @type_guid.setter
    def type_guid(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TypeGUID = next(unwrapped)

    @property
    def identifier(self) -> System.Guid:
        dotnet_result = self._dotnet_instance.Identifier
        return _wrap(dotnet_result)

    @identifier.setter
    def identifier(self, value: System.Guid):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Identifier = next(unwrapped)

    @overload
    def add_error(self, key: str, is_error: bool, err_code: int, message: str):
        ...

    def add_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_error(self, key: str):
        ...

    def remove_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_all_error(self):
        ...

    def remove_all_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveAllError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def duplicate_public_errors(self, other_node: BaseNodeType):
        ...

    def duplicate_public_errors(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DuplicatePublicErrors(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_all_errors(self) -> Sequence[ErrorEntry]:
        ...

    def get_all_errors(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.getAllErrors(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs):
        ...

    def on_collection_changed(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.OnCollectionChanged(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def compare_to(self, obj: Any) -> int:
        ...

    @overload
    def compare_to(self, other: BaseNodeType) -> int:
        ...

    def compare_to(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CompareTo(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_type(self) -> NodeType:
        ...

    def get_node_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_children(self, deep: bool, mode: TraversalMode) -> Sequence[BaseNodeType]:
        ...

    def get_node_children(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeChildren(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str]) -> Sequence[BaseNodeType]:
        ...

    @overload
    def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str], leaf_filter: ITraverseNodeFilter, branch_filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]:
        ...

    def get_sorted_node_children(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSortedNodeChildren(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_node_in_array(self, list: Sequence[BaseNodeType]) -> int:
        ...

    def find_node_in_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNodeInArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def filter_base_node_types(self, list: Sequence[BaseNodeType], filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]:
        ...

    def filter_base_node_types(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FilterBaseNodeTypes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def is_reference_same_object(self, node_to_compare: BaseNodeType) -> bool:
        ...

    def is_reference_same_object(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsReferenceSameObject(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def rename_node(self, new_name: str) -> bool:
        ...

    def rename_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RenameNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def is_node_relative(self, node_to_check: BaseNodeType) -> bool:
        ...

    def is_node_relative(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsNodeRelative(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def accept(self, visitor: IVisitor):
        ...

    @overload
    def accept(self, visitor_inspection: IVisitorWithInspection) -> IInspectorResult:
        ...

    def accept(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Accept(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_root(self) -> RootType:
        ...

    def get_node_root(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeRoot(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_parent(self) -> Tuple[bool, BaseNodeType]:
        ...

    def get_parent(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_duplicate_reference(self) -> BaseNodeType:
        ...

    def get_duplicate_reference(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDuplicateReference(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_node(self, id: int) -> Tuple[bool, BaseNodeType]:
        ...

    @overload
    def find_node(self, path: Sequence[str]) -> Tuple[bool, BaseNodeType]:
        ...

    def find_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_first_child_node_with_name(self, name: str) -> Tuple[bool, BaseNodeType]:
        ...

    def find_first_child_node_with_name(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindFirstChildNodeWithName(*unwrapped)
        return _wrap(dotnet_result)

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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNodeMatchGUID(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_nodesby_guid(self, guids: Sequence[str], recurse: bool, traversal_mode: TraversalMode) -> Tuple[bool, Sequence[BaseNodeType]]:
        ...

    def find_nodesby_guid(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNodesbyGUID(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_guid_up(self, guid: str) -> Tuple[bool, BaseNodeType]:
        ...

    @overload
    def find_guid_up(self, guid: Sequence[str]) -> Tuple[bool, BaseNodeType, str]:
        ...

    def find_guid_up(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindGUIDUp(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_node(self):
        ...

    @overload
    def remove_node(self, for_reuse: bool):
        ...

    def remove_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def move_node_to(self, new_parent: BaseNodeType) -> bool:
        ...

    def move_node_to(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.MoveNodeTo(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def attached_child_node(self, node_to_attached: BaseNodeType) -> bool:
        ...

    def attached_child_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AttachedChildNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_properties(self) -> Tuple[Sequence[str], Sequence[PropertyContent]]:
        ...

    def get_node_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_property_type(self, name: str) -> Tuple[bool, PropertyContent]:
        ...

    def get_node_property_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodePropertyType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_all_properties_with_type(self, prop_type: PropertyContent) -> Sequence[str]:
        ...

    def get_all_properties_with_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAllPropertiesWithType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def has_node_property(self, name: str) -> Tuple[bool, PropertyContent]:
        ...

    def has_node_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.HasNodeProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clear_properties(self):
        ...

    def clear_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ClearProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def duplicate_properties(self, other_node: BaseNodeType):
        ...

    def duplicate_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DuplicateProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_property(self, name: str, value: str) -> bool:
        ...

    def set_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_binary_string_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_binary_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBinaryStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_property(self, name: str, value: bool) -> bool:
        ...

    def set_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_property(self, name: str, value: int) -> bool:
        ...

    def set_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i16_property(self, name: str, value: int) -> bool:
        ...

    def set_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i64_property(self, name: str, value: int) -> bool:
        ...

    def set_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_property(self, name: str, value: int) -> bool:
        ...

    def set_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_property(self, name: str, value: int) -> bool:
        ...

    def set_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_property(self, name: str, value: float) -> bool:
        ...

    def set_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_property(self, name: str, value: int) -> bool:
        ...

    def set_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_variant_property(self, name: str, type: Sequence[int], data: Sequence[int]) -> bool:
        ...

    def set_variant_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetVariantProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_array_property(self, name: str, data: Sequence[float]) -> bool:
        ...

    def set_double_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_array_property(self, name: str, data: Sequence[bool]) -> bool:
        ...

    def set_boolean_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i64_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i16_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_array_property(self, name: str, data: Sequence[str]) -> bool:
        ...

    def set_string_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dictionary_property(self, name: str, data: DictionaryProperty) -> bool:
        ...

    def set_dictionary_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDictionaryProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dictionary_array_property(self, name: str, data: Sequence[DictionaryProperty]) -> bool:
        ...

    def set_dictionary_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDictionaryArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dependent_file_value(self, name: str, file_path: str, type: DependentFilePropertyType, version: str, force_download: bool, rt_dest: str, supported_target: str, md5: str) -> bool:
        ...

    def set_dependent_file_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDependentFileValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dependent_node_value(self, name: str, node: BaseNodeType) -> bool:
        ...

    @overload
    def set_dependent_node_value(self, name: str, node_path: str) -> bool:
        ...

    def set_dependent_node_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDependentNodeValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_data_source_value(self, name: str, node: BaseNodeType) -> bool:
        ...

    @overload
    def set_data_source_value(self, name: str, node_path: str) -> bool:
        ...

    def set_data_source_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDataSourceValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_property(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_binary_string_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_binary_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBinaryStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_property(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double_property(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_variant_value(self, name: str) -> Tuple[bool, Sequence[int], Sequence[int]]:
        ...

    def get_variant_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetVariantValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double_array_property(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_double_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_array_property(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_boolean_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_array_property(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_string_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dictionary_property(self, name: str) -> Tuple[bool, DictionaryProperty]:
        ...

    def get_dictionary_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDictionaryProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dictionary_array_property(self, name: str) -> Tuple[bool, Sequence[DictionaryProperty]]:
        ...

    def get_dictionary_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDictionaryArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

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
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

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
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

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
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

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
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

    @overload
    def get_dependent_file_value(self, name: str) -> Tuple[bool, str, DependentFilePropertyType, str, bool, str, str, str]:
        ...

    def get_dependent_file_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDependentFileValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_property(self, name: str) -> bool:
        ...

    def remove_property(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.RemoveProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clone(self) -> BaseNodeType:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def shallow_copy(self) -> BaseNodeType:
        ...

    def shallow_copy(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ShallowCopy(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def deep_copy(self) -> BaseNodeType:
        ...

    def deep_copy(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DeepCopy(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def start_monitoring_dependent(self, dependent: BaseNodeType, id: str):
        ...

    def start_monitoring_dependent(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.startMonitoringDependent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def stop_monitoring_dependent(self, dependent: BaseNodeType, id: str):
        ...

    def stop_monitoring_dependent(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.stopMonitoringDependent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_observing_nodes(self) -> Iterable[BaseNodeType]:
        ...

    def get_observing_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetObservingNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def notify_observing_nodes(self, arg: OnNodeChangeEventArgs):
        ...

    def notify_observing_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.notifyObservingNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def get_enumerator(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetEnumerator(*unwrapped)
        return _wrap(dotnet_result)

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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_STRING")
        return PropertyContent(dotnet_result, "K_STRING")

    @_staticproperty
    def K_BOOL() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BOOL")
        return PropertyContent(dotnet_result, "K_BOOL")

    @_staticproperty
    def K_I32() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I32")
        return PropertyContent(dotnet_result, "K_I32")

    @_staticproperty
    def K_U32() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U32")
        return PropertyContent(dotnet_result, "K_U32")

    @_staticproperty
    def K_DOUBLE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DOUBLE")
        return PropertyContent(dotnet_result, "K_DOUBLE")

    @_staticproperty
    def K_U64() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U64")
        return PropertyContent(dotnet_result, "K_U64")

    @_staticproperty
    def K_VARIANT() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_VARIANT")
        return PropertyContent(dotnet_result, "K_VARIANT")

    @_staticproperty
    def K_DEPENDENTFILE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DEPENDENTFILE")
        return PropertyContent(dotnet_result, "K_DEPENDENTFILE")

    @_staticproperty
    def K_DEPENDENTNODE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DEPENDENTNODE")
        return PropertyContent(dotnet_result, "K_DEPENDENTNODE")

    @_staticproperty
    def K_DATASOURCENODE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DATASOURCENODE")
        return PropertyContent(dotnet_result, "K_DATASOURCENODE")

    @_staticproperty
    def K_U16() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U16")
        return PropertyContent(dotnet_result, "K_U16")

    @_staticproperty
    def K_DBLARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DBLARR")
        return PropertyContent(dotnet_result, "K_DBLARR")

    @_staticproperty
    def K_U32_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U32ARR")
        return PropertyContent(dotnet_result, "K_U32_ARR")

    @_staticproperty
    def K_I32_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I32ARR")
        return PropertyContent(dotnet_result, "K_I32_ARR")

    @_staticproperty
    def K_STRINGARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_STRINGARR")
        return PropertyContent(dotnet_result, "K_STRINGARR")

    @_staticproperty
    def K_DICTIONARY() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DICTIONARY")
        return PropertyContent(dotnet_result, "K_DICTIONARY")

    @_staticproperty
    def K_DICTIONARYARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DICTIONARYARR")
        return PropertyContent(dotnet_result, "K_DICTIONARYARR")

    @_staticproperty
    def K_BINARYSTRING() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BINARYSTRING")
        return PropertyContent(dotnet_result, "K_BINARYSTRING")

    @_staticproperty
    def K_I16() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I16")
        return PropertyContent(dotnet_result, "K_I16")

    @_staticproperty
    def K_I64() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I64")
        return PropertyContent(dotnet_result, "K_I64")

    @_staticproperty
    def K_BOOLARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BOOLARR")
        return PropertyContent(dotnet_result, "K_BOOLARR")

    @_staticproperty
    def K_U64_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U64ARR")
        return PropertyContent(dotnet_result, "K_U64_ARR")

    @_staticproperty
    def K_U16_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U16ARR")
        return PropertyContent(dotnet_result, "K_U16_ARR")

    @_staticproperty
    def K_I64_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I64ARR")
        return PropertyContent(dotnet_result, "K_I64_ARR")

    @_staticproperty
    def K_I16_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I16ARR")
        return PropertyContent(dotnet_result, "K_I16_ARR")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType, "Double")
        return WaveformTypeDataType(dotnet_result, "DOUBLE")

    @_staticproperty
    def COMPLEX_DOUBLE() -> WaveformTypeDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType, "ComplexDouble")
        return WaveformTypeDataType(dotnet_result, "COMPLEX_DOUBLE")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DocumentType(*unwrapped)

    @property
    def no_namespace_schema_location(self) -> str:
        dotnet_result = self._dotnet_instance.noNamespaceSchemaLocation
        return _wrap(dotnet_result)

    @no_namespace_schema_location.setter
    def no_namespace_schema_location(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.noNamespaceSchemaLocation = next(unwrapped)

    @_staticproperty
    def project_version() -> Tuple[int, int, int, int]:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.ProjectVersion
        return _wrap(dotnet_result)

    @_staticproperty
    def schema_uri() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.SchemaUri
        return _wrap(dotnet_result)

    @property
    def storage_watcher(self) -> SystemStorageWatcher:
        dotnet_result = self._dotnet_instance.StorageWatcher
        return _wrap(dotnet_result)

    @property
    def document_file_path(self) -> str:
        """Access the document file path."""
        dotnet_result = self._dotnet_instance.DocumentFilePath
        return _wrap(dotnet_result)

    @document_file_path.setter
    def document_file_path(self, value: str):
        """Access the document file path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DocumentFilePath = next(unwrapped)

    @property
    def md5_checksum(self) -> str:
        dotnet_result = self._dotnet_instance.MD5Checksum
        return _wrap(dotnet_result)

    @md5_checksum.setter
    def md5_checksum(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MD5Checksum = next(unwrapped)

    @property
    def version(self) -> VersionType:
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: VersionType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def content(self) -> DocumentTypeContent:
        dotnet_result = self._dotnet_instance.Content
        return _wrap(dotnet_result)

    @content.setter
    def content(self, value: DocumentTypeContent):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Content = next(unwrapped)

    @property
    def item(self) -> BaseNodeType:
        dotnet_result = self._dotnet_instance.Item
        return _wrap(dotnet_result)

    @item.setter
    def item(self, value: BaseNodeType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Item = next(unwrapped)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def save_system_storage_file(self) -> Tuple[bool, str]:
        ...

    @overload
    def save_system_storage_file(self, filepath: str) -> Tuple[bool, str]:
        ...

    def save_system_storage_file(self, *args):
        unwrapped = _unwrap({(): (0, ""), (str,): (1, "")}, *args)
        dotnet_result = self._dotnet_instance.SaveSystemStorageFile(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def load_system_storage_file(self, filepath: str, schemapath: str) -> Tuple[bool, str]:
        ...

    @overload
    def load_system_storage_file(self, filepath: str, schemapath: str, version_to_mutate: Sequence[XMLVersionInfo], xslst_file_paths: Sequence[str]) -> Tuple[bool, str]:
        ...

    def load_system_storage_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.LoadSystemStorageFile(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def load_project_xml_file(self, filepath: str) -> Tuple[bool, str, bool]:
        ...

    def load_project_xml_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.LoadProjectXMLFile(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def get_system_definition_file_path(project_file_path: str) -> str:
        ...

    def get_system_definition_file_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.GetSystemDefinitionFilePath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_content(self, node: BaseNodeType):
        ...

    def set_content(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetContent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_duplicate_reference(self) -> DocumentType:
        ...

    def get_duplicate_reference(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDuplicateReference(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def read_version_info(version_tag: str, file_path: str) -> XMLVersionInfo:
        ...

    def read_version_info(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.ReadVersionInfo(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.VersionType(*unwrapped)

    @property
    def major(self) -> int:
        dotnet_result = self._dotnet_instance.Major
        return _wrap(dotnet_result)

    @major.setter
    def major(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Major = next(unwrapped)

    @property
    def minor(self) -> int:
        dotnet_result = self._dotnet_instance.Minor
        return _wrap(dotnet_result)

    @minor.setter
    def minor(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Minor = next(unwrapped)

    @property
    def fix(self) -> int:
        dotnet_result = self._dotnet_instance.Fix
        return _wrap(dotnet_result)

    @fix.setter
    def fix(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Fix = next(unwrapped)

    @property
    def build(self) -> int:
        dotnet_result = self._dotnet_instance.Build
        return _wrap(dotnet_result)

    @build.setter
    def build(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Build = next(unwrapped)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "Absolute")
        return DependentFilePropertyType(dotnet_result, "ABSOLUTE")

    @_staticproperty
    def RELATIVE() -> DependentFilePropertyType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "Relative")
        return DependentFilePropertyType(dotnet_result, "RELATIVE")

    @_staticproperty
    def TO_COMMON_DOC_DIR() -> DependentFilePropertyType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "ToCommonDocDir")
        return DependentFilePropertyType(dotnet_result, "TO_COMMON_DOC_DIR")

    @_staticproperty
    def TO_APPLICATION_DATA_DIR() -> DependentFilePropertyType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "ToApplicationDataDir")
        return DependentFilePropertyType(dotnet_result, "TO_APPLICATION_DATA_DIR")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ErrorEntry(*unwrapped)

    @property
    def message(self) -> str:
        dotnet_result = self._dotnet_instance.Message
        return _wrap(dotnet_result)

    @message.setter
    def message(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Message = next(unwrapped)

    @property
    def key(self) -> str:
        dotnet_result = self._dotnet_instance.Key
        return _wrap(dotnet_result)

    @key.setter
    def key(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Key = next(unwrapped)

    @property
    def is_error(self) -> bool:
        dotnet_result = self._dotnet_instance.IsError
        return _wrap(dotnet_result)

    @is_error.setter
    def is_error(self, value: bool):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IsError = next(unwrapped)

    @property
    def code(self) -> int:
        dotnet_result = self._dotnet_instance.Code
        return _wrap(dotnet_result)

    @code.setter
    def code(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Code = next(unwrapped)

    @overload
    def clone(self) -> ErrorEntry:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def equals(self, other: ErrorEntry) -> bool:
        ...

    @overload
    def equals(self, obj: Any) -> bool:
        ...

    def equals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Equals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_hash_code(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetHashCode(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.PropertyType(*unwrapped)

    @property
    def type(self) -> PropertyContent:
        """Akin to reflection method to return the actual property type."""
        dotnet_result = self._dotnet_instance.Type
        return _wrap(dotnet_result)

    @property
    def item(self) -> Any:
        dotnet_result = self._dotnet_instance.Item
        return _wrap(dotnet_result)

    @item.setter
    def item(self, value: Any):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Item = next(unwrapped)

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @name.setter
    def name(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Name = next(unwrapped)

    @overload
    def clone(self) -> PropertyType:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_BASE")
        return NodeType(dotnet_result, "K_BASE")

    @_staticproperty
    def K_ALIAS() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_ALIAS")
        return NodeType(dotnet_result, "K_ALIAS")

    @_staticproperty
    def K_CHANNEL() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_CHANNEL")
        return NodeType(dotnet_result, "K_CHANNEL")

    @_staticproperty
    def K_SECTION() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_SECTION")
        return NodeType(dotnet_result, "K_SECTION")

    @_staticproperty
    def K_TARGET() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_TARGET")
        return NodeType(dotnet_result, "K_TARGET")

    @_staticproperty
    def K_TARGETSECTION() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_TARGETSECTION")
        return NodeType(dotnet_result, "K_TARGETSECTION")

    @_staticproperty
    def K_ROOT() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_ROOT")
        return NodeType(dotnet_result, "K_ROOT")

    @_staticproperty
    def K_WAVEFORM() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_WAVEFORM")
        return NodeType(dotnet_result, "K_WAVEFORM")

    @_staticproperty
    def K_PARAMETER() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_PARAMETER")
        return NodeType(dotnet_result, "K_PARAMETER")


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_BFS")
        return TraversalMode(dotnet_result, "K_BFS")

    @_staticproperty
    def K_DFS() -> TraversalMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_DFS")
        return TraversalMode(dotnet_result, "K_DFS")

    @_staticproperty
    def K_CHILDONLY() -> TraversalMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_CHILDONLY")
        return TraversalMode(dotnet_result, "K_CHILDONLY")

    @_staticproperty
    def K_UP() -> TraversalMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_UP")
        return TraversalMode(dotnet_result, "K_UP")


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CheckWithFilter(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Visit(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Visit(*unwrapped)
        return _wrap(dotnet_result)


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
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Result(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.RootType(*unwrapped)

    @property
    def target_sections(self) -> TargetSectionsType:
        dotnet_result = self._dotnet_instance.TargetSections
        return _wrap(dotnet_result)

    @target_sections.setter
    def target_sections(self, value: TargetSectionsType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TargetSections = next(unwrapped)

    @property
    def section(self) -> Sequence[SectionType]:
        dotnet_result = self._dotnet_instance.Section
        return _wrap(dotnet_result)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Section = next(unwrapped)

    @overload
    def get_owning_document_file_path(self) -> str:
        ...

    def get_owning_document_file_path(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOwningDocumentFilePath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def refresh_node_dependencies(self):
        ...

    def refresh_node_dependencies(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RefreshNodeDependencies(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_target_section(self, new_target_section: TargetSectionsType) -> bool:
        ...

    @overload
    def set_target_section(self, new_target_section: TargetSectionsType, relink: bool) -> bool:
        ...

    def set_target_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetTargetSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleSectionType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.BaseCustomNodeProperty(*unwrapped)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clone(self) -> BaseCustomNodeProperty:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DictionaryProperty(*unwrapped)

    @property
    def count(self) -> int:
        dotnet_result = self._dotnet_instance.Count
        return _wrap(dotnet_result)

    @property
    def elem(self) -> Sequence[DictionaryElement]:
        dotnet_result = self._dotnet_instance.Elem
        return _wrap(dotnet_result)

    @elem.setter
    def elem(self, value: Sequence[DictionaryElement]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Elem = next(unwrapped)

    @overload
    def clear(self):
        ...

    def clear(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clear(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_element(self, key: str) -> bool:
        ...

    def remove_element(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveElement(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_string(self, name: str, value: str) -> bool:
        ...

    def add_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_boolean(self, name: str, value: bool) -> bool:
        ...

    def add_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i32(self, name: str, value: int) -> bool:
        ...

    def add_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i16(self, name: str, value: int) -> bool:
        ...

    def add_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i64(self, name: str, value: int) -> bool:
        ...

    def add_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u32(self, name: str, value: int) -> bool:
        ...

    def add_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u16(self, name: str, value: int) -> bool:
        ...

    def add_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_double(self, name: str, value: float) -> bool:
        ...

    def add_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u64(self, name: str, value: int) -> bool:
        ...

    def add_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_double(self, name: str, value: Sequence[float]) -> bool:
        ...

    def add_arr_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_boolean(self, name: str, value: Sequence[bool]) -> bool:
        ...

    def add_arr_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_u64(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_u32(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_u16(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_i64(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_i32(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_i16(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_string(self, name: str, value: Sequence[str]) -> bool:
        ...

    def add_arr_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_bool(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_bool(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBool(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_double(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_arr_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_boolean(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_arr_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_u64(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_u32(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_u16(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_i64(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_i32(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_i16(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_string(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_arr_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrString(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs(*unwrapped)

    @_staticproperty
    def k_deleted() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_DELETED
        return _wrap(dotnet_result)

    @_staticproperty
    def k_error() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_ERROR
        return _wrap(dotnet_result)

    @_staticproperty
    def k_no_error() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_NO_ERROR
        return _wrap(dotnet_result)

    @_staticproperty
    def k_property_changed() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_PROPERTY_CHANGED
        return _wrap(dotnet_result)

    @_staticproperty
    def k_collection_changed() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_COLLECTION_CHANGED
        return _wrap(dotnet_result)

    @property
    def m_action(self) -> str:
        """public field to access the action"""
        dotnet_result = self._dotnet_instance.m_action
        return _wrap(dotnet_result)

    @property
    def m_data(self) -> Sequence[int]:
        """public field to access the generic data field."""
        dotnet_result = self._dotnet_instance.m_data
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ChannelType(*unwrapped)

    @property
    def is_readable(self) -> bool:
        """field to indicate if channel is readable"""
        dotnet_result = self._dotnet_instance.IsReadable
        return _wrap(dotnet_result)

    @property
    def is_writable(self) -> bool:
        """field to indicate if channel is writable"""
        dotnet_result = self._dotnet_instance.IsWritable
        return _wrap(dotnet_result)

    @property
    def is_faultable(self) -> bool:
        """field to indicate if channel is faultable"""
        dotnet_result = self._dotnet_instance.IsFaultable
        return _wrap(dotnet_result)

    @property
    def is_scalable(self) -> bool:
        """field to indicate if channel is scalable"""
        dotnet_result = self._dotnet_instance.IsScalable
        return _wrap(dotnet_result)

    @property
    def data_length(self) -> int:
        """return the data length of the channel."""
        dotnet_result = self._dotnet_instance.DataLength
        return _wrap(dotnet_result)

    @property
    def default_value(self) -> Sequence[float]:
        dotnet_result = self._dotnet_instance.DefaultValue
        return _wrap(dotnet_result)

    @default_value.setter
    def default_value(self, value: Sequence[float]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DefaultValue = next(unwrapped)

    @property
    def row_dim(self) -> int:
        dotnet_result = self._dotnet_instance.RowDim
        return _wrap(dotnet_result)

    @row_dim.setter
    def row_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RowDim = next(unwrapped)

    @property
    def col_dim(self) -> int:
        dotnet_result = self._dotnet_instance.ColDim
        return _wrap(dotnet_result)

    @col_dim.setter
    def col_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ColDim = next(unwrapped)

    @property
    def units(self) -> str:
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @units.setter
    def units(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Units = next(unwrapped)

    @property
    def bit_fields(self) -> int:
        dotnet_result = self._dotnet_instance.BitFields
        return _wrap(dotnet_result)

    @bit_fields.setter
    def bit_fields(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BitFields = next(unwrapped)

    @overload
    def is_under_target(self, target_to_check: TargetType) -> bool:
        ...

    def is_under_target(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsUnderTarget(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def get_value_table(channel: ChannelType) -> Tuple[bool, Sequence[str], Sequence[float]]:
        ...

    def get_value_table(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.ChannelType.GetValueTable(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def set_value_table(channel: ChannelType, names: Sequence[str], values: Sequence[float]):
        ...

    def set_value_table(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.ChannelType.SetValueTable(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.SystemStorageWatcher.K_SYSTEM_STORAGE_WATCHER_DEPENDENTID
        return _wrap(dotnet_result)

    @property
    def error_count(self) -> int:
        """Gets the current error count"""
        dotnet_result = self._dotnet_instance.ErrorCount
        return _wrap(dotnet_result)

    @property
    def has_modification(self) -> bool:
        dotnet_result = self._dotnet_instance.HasModification
        return _wrap(dotnet_result)

    @property
    def error_in_system(self) -> Sequence[BaseNodeType]:
        dotnet_result = self._dotnet_instance.ErrorInSystem
        return _wrap(dotnet_result)

    @property
    def has_any_error(self) -> bool:
        dotnet_result = self._dotnet_instance.HasAnyError
        return _wrap(dotnet_result)

    @overload
    def reset_modification_flag(self):
        ...

    def reset_modification_flag(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ResetModificationFlag(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def fire_count_event(self):
        ...

    def fire_count_event(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FireCountEvent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def supress_notification(self):
        ...

    def supress_notification(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SupressNotification(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def unsupress_notification(self):
        ...

    def unsupress_notification(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.UnsupressNotification(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def is_node_in_error_collection(self, node: BaseNodeType) -> bool:
        ...

    def is_node_in_error_collection(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsNodeInErrorCollection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "Definition")
        return DocumentTypeContent(dotnet_result, "DEFINITION")

    @_staticproperty
    def EXPORT() -> DocumentTypeContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "Export")
        return DocumentTypeContent(dotnet_result, "EXPORT")

    @_staticproperty
    def SLSC() -> DocumentTypeContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "SLSC")
        return DocumentTypeContent(dotnet_result, "SLSC")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.SectionType(*unwrapped)

    @property
    def section(self) -> Sequence[SectionType]:
        dotnet_result = self._dotnet_instance.Section
        return _wrap(dotnet_result)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Section = next(unwrapped)

    @property
    def channel(self) -> Sequence[ChannelType]:
        dotnet_result = self._dotnet_instance.Channel
        return _wrap(dotnet_result)

    @channel.setter
    def channel(self, value: Sequence[ChannelType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Channel = next(unwrapped)

    @property
    def alias(self) -> Sequence[AliasType]:
        dotnet_result = self._dotnet_instance.Alias
        return _wrap(dotnet_result)

    @alias.setter
    def alias(self, value: Sequence[AliasType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Alias = next(unwrapped)

    @property
    def parameter(self) -> Sequence[ParameterType]:
        dotnet_result = self._dotnet_instance.Parameter
        return _wrap(dotnet_result)

    @parameter.setter
    def parameter(self, value: Sequence[ParameterType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Parameter = next(unwrapped)

    @property
    def waveform(self) -> Sequence[WaveformType]:
        dotnet_result = self._dotnet_instance.Waveform
        return _wrap(dotnet_result)

    @waveform.setter
    def waveform(self, value: Sequence[WaveformType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Waveform = next(unwrapped)

    @overload
    def attached_child_node_without_check(self, node: BaseNodeType):
        ...

    def attached_child_node_without_check(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AttachedChildNodeWithoutCheck(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleSectionType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_channel_type(self, new_nodes: Sequence[ChannelType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_channel_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleChannelType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_channel_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_channel_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderChannelTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_channel_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_channel_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChannelTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_alias_type(self, new_nodes: Sequence[AliasType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_alias_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleAliasType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_alias_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_alias_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderAliasTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alias_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_alias_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAliasTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_parameter_type(self, new_nodes: Sequence[ParameterType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_parameter_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleParameterType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_parameter_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_parameter_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderParameterTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_parameter_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_parameter_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParameterTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_waveform_type(self, new_nodes: Sequence[WaveformType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_waveform_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleWaveformType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_waveform_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_waveform_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderWaveformTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_waveform_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_waveform_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetWaveformTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.AliasType(*unwrapped)

    @property
    def resolve_alias_reference(self) -> BaseNodeType:
        """Gets the referenced channel."""
        dotnet_result = self._dotnet_instance.ResolveAliasReference
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ParameterType(*unwrapped)

    @property
    def row_dim(self) -> int:
        dotnet_result = self._dotnet_instance.RowDim
        return _wrap(dotnet_result)

    @row_dim.setter
    def row_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RowDim = next(unwrapped)

    @property
    def col_dim(self) -> int:
        dotnet_result = self._dotnet_instance.ColDim
        return _wrap(dotnet_result)

    @col_dim.setter
    def col_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ColDim = next(unwrapped)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.TargetType(*unwrapped)

    @property
    def dfs_object_enumerator(self) -> System.Collections.IEnumerator:
        """Return a non generic Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found."""
        dotnet_result = self._dotnet_instance.DFSObjectEnumerator
        return _wrap(dotnet_result)

    @property
    def section(self) -> Sequence[SectionType]:
        dotnet_result = self._dotnet_instance.Section
        return _wrap(dotnet_result)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Section = next(unwrapped)

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleSectionType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.TargetSectionsType(*unwrapped)

    @property
    def target(self) -> Sequence[TargetType]:
        dotnet_result = self._dotnet_instance.Target
        return _wrap(dotnet_result)

    @target.setter
    def target(self, value: Sequence[TargetType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Target = next(unwrapped)

    @overload
    def add_multiple_target_type(self, new_nodes: Sequence[TargetType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_target_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleTargetType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_target_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_target_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderTargetTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_target_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_target_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTargetTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


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
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "Assert")
        return DuplicateOp(dotnet_result, "ASSERT")

    @_staticproperty
    def RENAME() -> DuplicateOp:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "Rename")
        return DuplicateOp(dotnet_result, "RENAME")

    @_staticproperty
    def UNIQUE_ONLY() -> DuplicateOp:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "UniqueOnly")
        return DuplicateOp(dotnet_result, "UNIQUE_ONLY")


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DictionaryElement(*unwrapped)

    @property
    def item(self) -> Any:
        dotnet_result = self._dotnet_instance.Item
        return _wrap(dotnet_result)

    @item.setter
    def item(self, value: Any):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Item = next(unwrapped)

    @property
    def key(self) -> str:
        dotnet_result = self._dotnet_instance.Key
        return _wrap(dotnet_result)

    @key.setter
    def key(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Key = next(unwrapped)

    @overload
    def clone(self) -> DictionaryElement:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)


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
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.WaveformType(*unwrapped)

    @property
    def data_type(self) -> WaveformTypeDataType:
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @data_type.setter
    def data_type(self, value: WaveformTypeDataType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataType = next(unwrapped)

    @property
    def units(self) -> str:
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @units.setter
    def units(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Units = next(unwrapped)
