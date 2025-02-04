[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# UnityEngine.PropertiesModule

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Interfaces and utilities to describe and visit data containers.

### Classes

[ArrayPropertyBag<T0>](Unity.Properties.ArrayPropertyBag_1.html)|  An
IPropertyBag_1 implementation for a built in array of TElement.  
---|---  
[ConcreteTypeVisitor](Unity.Properties.ConcreteTypeVisitor.html)|  Base class
to implement a visitor responsible for getting an object's concrete type as a
generic.  
[ContainerPropertyBag<T0>](Unity.Properties.ContainerPropertyBag_1.html)|
Base class for implementing a static property bag for a specified container
type. This is an abstract class.  
[CreatePropertyAttribute](Unity.Properties.CreatePropertyAttribute.html)|  Use
this attribute to have a property generated for the member.  
[DelegateProperty<T0,T1>](Unity.Properties.DelegateProperty_2.html)|
Represents a value property.  
[DictionaryPropertyBag<T0,T1>](Unity.Properties.DictionaryPropertyBag_2.html)|
An IPropertyBag_1 implementation for a Dictionary_2 type.  
[DontCreatePropertyAttribute](Unity.Properties.DontCreatePropertyAttribute.html)|
Use this attribute to prevent have a property from being automatically
generated on a public field.  
[GeneratePropertyBagAttribute](Unity.Properties.GeneratePropertyBagAttribute.html)|
Use this attribute to have the source generator generate property bags for a
given type.  
[GeneratePropertyBagsForAssemblyAttribute](Unity.Properties.GeneratePropertyBagsForAssemblyAttribute.html)|
Use this attribute to enable the source generator to run on this assembly.  
[GeneratePropertyBagsForTypeAttribute](Unity.Properties.GeneratePropertyBagsForTypeAttribute.html)|
Use this attribute to have the source generator generate a property bag for a
given type. This attribute works for the specified type ONLY, it does NOT
include derived types.  
[GeneratePropertyBagsForTypesQualifiedWithAttribute](Unity.Properties.GeneratePropertyBagsForTypesQualifiedWithAttribute.html)|
Use this attribute to have the properties source generator generate property
bags for types implementing the specified interface.  
[HashSetPropertyBag<T0>](Unity.Properties.HashSetPropertyBag_1.html)|  An
IPropertyBag_1 implementation for a HashSet_1 type.  
[IndexedCollectionPropertyBag<T0,T1>](Unity.Properties.IndexedCollectionPropertyBag_2.html)|
An IPropertyBag_1 implementation for a generic collection of elements which
can be accessed by index. This is based on the IList_1 interface.  
[InvalidContainerTypeException](Unity.Properties.InvalidContainerTypeException.html)|
The exception that is thrown when trying to visit an invalid container type.  
[InvalidPathException](Unity.Properties.InvalidPathException.html)|  The
exception that is thrown when trying to resolve an invalid path.  
[KeyValueCollectionPropertyBag<T0,T1,T2>](Unity.Properties.KeyValueCollectionPropertyBag_3.html)|
An IPropertyBag_1 implementation for a generic collection of key/value pairs
using the IDictionary_2 interface.  
[KeyValuePairPropertyBag<T0,T1>](Unity.Properties.KeyValuePairPropertyBag_2.html)|
A IPropertyBag_1 implementation for a generic key/value pair.  
[ListPropertyBag<T0>](Unity.Properties.ListPropertyBag_1.html)|  A
IPropertyBag_1 implementation for a List_1 type.  
[MissingPropertyBagException](Unity.Properties.MissingPropertyBagException.html)|
The exception that is thrown when trying to visit a container with no property
bag.  
[PathVisitor](Unity.Properties.PathVisitor.html)|  Helper visitor to visit a
single property using a specified PropertyPath.  
[Property<T0,T1>](Unity.Properties.Property_2.html)|  Base class for
implementing properties. This is an abstract class.  
[PropertyBag](Unity.Properties.PropertyBag.html)|  The PropertyBag class
provides access to registered property bag instances.  
[PropertyBag<T0>](Unity.Properties.PropertyBag_1.html)|  Base class for
implementing a property bag for a specified container type. This is an
abstract class.  
[PropertyContainer](Unity.Properties.PropertyContainer.html)|  The
PropertyContainer class is used as the entry point to operate on data
containers using properties.  
[PropertyVisitor](Unity.Properties.PropertyVisitor.html)|  Base class for
implementing algorithms using properties. This is an abstract class.  
[ReflectedMemberProperty<T0,T1>](Unity.Properties.ReflectedMemberProperty_2.html)|
A ReflectedMemberProperty_2 provides strongly typed access to an underlying
FieldInfo or PropertyInfo object.  
[SetPropertyBagBase<T0,T1>](Unity.Properties.SetPropertyBagBase_2.html)|  A
IPropertyBag_1 implementation for a generic set of elements using the ISet_1
interface.  
[TypeConversion](Unity.Properties.TypeConversion.html)|  Helper class to
handle type conversion during properties API calls.  
[TypeTraits](Unity.Properties.TypeTraits.html)|  Helper class to avoid paying
the cost of runtime type lookups.  
[TypeTraits<T0>](Unity.Properties.TypeTraits_1.html)|  Helper class to avoid
paying the cost of runtime type lookups. This is also used to abstract
underlying type info in the runtime (e.g. RuntimeTypeHandle vs StaticTypeReg)  
[TypeUtility](Unity.Properties.TypeUtility.html)|  Utility class around
System.Type.  
  
### Structs

[AttributesScope](Unity.Properties.AttributesScope.html)|  Scope for using a
given set of attributes.  
---|---  
[ExcludeContext<T0,T1>](Unity.Properties.ExcludeContext_2.html)|  Context
object used during visitation to determine if a property should be visited or
not.  
[ExcludeContext<T0>](Unity.Properties.ExcludeContext_1.html)|  Context object
used during visitation to determine if a property should be visited or not.  
[PropertyCollection<T0>](Unity.Properties.PropertyCollection_1.html)|  The
PropertyCollection_1 struct provides enumerable access to all IProperty_1 for
a given PropertyBag_1.  
[PropertyPath](Unity.Properties.PropertyPath.html)|  A PropertyPath is used to
store a reference to a single property within a tree.  
[PropertyPathPart](Unity.Properties.PropertyPathPart.html)|  A
PropertyPathPart represents a single element of the path.  
[VisitContext<T0,T1>](Unity.Properties.VisitContext_2.html)|  Context object
used during visitation when a IProperty_1 is visited.  
[VisitContext<T0>](Unity.Properties.VisitContext_1.html)|  Context object used
during visitation when a IProperty_1 is visited.  
[VisitParameters](Unity.Properties.VisitParameters.html)|  Custom parameters
to use for visitation.  
  
### Enumerations

[InstantiationKind](Unity.Properties.InstantiationKind.html)|  Describes how a
new instance is created.  
---|---  
[PropertyPathPartKind](Unity.Properties.PropertyPathPartKind.html)|  A
PropertyPathPartKind specifies a type for a PropertyPathPart.  
[TypeGenerationOptions](Unity.Properties.TypeGenerationOptions.html)|  A set
of options to customize the behaviour of the code generator.  
[VisitExceptionKind](Unity.Properties.VisitExceptionKind.html)|  Flags used to
specify a set of exceptions.  
[VisitReturnCode](Unity.Properties.VisitReturnCode.html)|  Internal return
code used during path visitation.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

