[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/property-bags.html)
  * [中文](/cn/current/Manual/property-bags.html)
  * [日本語](/ja/current/Manual/property-bags.html)
  * [한국어](/kr/current/Manual/property-bags.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/property-bags.html)
  * [中文](/cn/current/Manual/property-bags.html)
  * [日本語](/ja/current/Manual/property-bags.html)
  * [한국어](/kr/current/Manual/property-bags.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Adding functionality to objects at runtime](properties.html)
  * Property bags

[](properties.html)

Adding functionality to objects at runtime

[](property-visitors.html)

Property visitors

# Property bags

Property bags are collections of properties for a given .Net object type that
you can use to access and set data for an instance of an object of that type.

## Concept

A property bag for a given type is a companion object that enables efficient
data traversal algorithms based on instances of that type. By default, Unity
uses reflection to generate the property bag for a type. This reflective
approach offers convenience and occurs lazily only once per type when a
property bag hasn’t been registered yet.

To enhance performance, you can opt-in to code generation by tagging the type
with
[`[Unity.Properties.GeneratePropertyBag]`](../ScriptReference/Unity.Properties.GeneratePropertyBagAttribute.html).
Additionally, to activate code generation, you must tag the assembly with
[`[assembly:
Unity.Properties.GeneratePropertyBagsForAssembly]`](../ScriptReference/Unity.Properties.GeneratePropertyBagsForAssemblyAttribute.html).
Code-generated property bags are automatically registered when the domain is
loaded.

In both the reflection and code-generation scenarios, the property bag
generates properties for the following:

  * Public fields
  * Private or internal fields tagged with [`[SerializeField]`](../ScriptReference/SerializeField.html), [`[SerializeReference]`](../ScriptReference/SerializeReference.html), or [`[CreateProperty]`](../ScriptReference/Unity.Properties.CreatePropertyAttribute.html)
  * Public, private, or internal properties tagged with [`[Unity.Properties.CreateProperty]`](../ScriptReference/Unity.Properties.CreatePropertyAttribute.html)

The property bag doesn’t generate a property for public, private, or internal
fields tagged with
[`[DontCreateProperty]`](../ScriptReference/Unity.Properties.DontCreatePropertyAttribute.html).

A generated property is read-only if the field is read-only or the property
only has a getter.

You can also use [`[Unity.Properties.CreateProperty(ReadOnly =
true)]`](../ScriptReference/Unity.Properties.DontCreatePropertyAttribute.html)
to make a generated property read-only.

Creating properties in the property bag using serialization attributes for
convenience is not always the preferred approach. Unity’s serialization system
can only operate on fields and auto-properties, which makes it challenging to
achieve validation or propagate changes effectively.

The following example combines the Unity serialization system with the Unity
Properties system:

    
    
    using UnityEngine;
    using Unity.Properties;
    
    public class MyBehaviour : MonoBehaviour
    {
        // Serializations go through the field, but we don't want to create a property for it.
        [SerializeField, DontCreateProperty] 
        private int m_Value;
        
        // For the property bag, use the property instead of the field. This ensures that
        // the value stays within the appropriate bounds.
        [CreateProperty] 
        public int value
        {
            get => m_Value;
            set => m_Value = value;
        }
        
        // This is a similar example, but for an auto-property.
        [field: SerializeField, DontCreateProperty]
        [CreateProperty]
        public float floatValue { get; set; }
    }
    

Unlike the Unity serialization system, the properties within a property bag
don’t qualify as value types with
[`[SerializeField]`](../ScriptReference/SerializeField.html). Instead, struct
types are recognized as value types, whereas class types are recognized as
references.

In Unity serialization, although polymorphism is supported, you must use the
[`[SerializeReference]`](../ScriptReference/SerializeReference.html) attribute
to explicitly opt in. Otherwise, instances are serialized as value types. It’s
worth noting that [`UnityEngine.Object`](../ScriptReference/Object.html) types
are an exception to this rule, as they’re automatically serialized as
reference types.

## Performance considerations

Unity Properties uses .Net reflection to create property bags and properties
that are strongly typed, which can introduce performance overhead the first
time you request a property bag for a given container type.

When you create properties for field members through reflection, these
properties may allocate garbage in **IL2CPP** A Unity-developed scripting
back-end which you can use as an alternative to Mono when building projects
for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) builds. This allocation occurs due to
the direct use of
[`System.Reflection.FieldInfo`](https://learn.microsoft.com/en-
us/dotnet/api/system.reflection.fieldinfo), which leads to unavoidable boxing.

To avoid reflection, you can code-generate property bags during compilation.
However, be aware that this optimization may lead to longer compilation times.
To enable code generation for an assembly, tag the assembly with
[`[Unity.Properties.GeneratePropertyBagsForAssemblyAttribute]`](../ScriptReference/Unity.Properties.GeneratePropertyBagsForAssemblyAttribute.html)
and tag individual types with
[`[Unity.Properties.GeneratePropertyBagAttribute]`](../ScriptReference/Unity.Properties.GeneratePropertyBagAttribute.html).
To enable the property bag to access internal, and private fields and
properties, make the type `partial`.

## Additional resources

  * [Property visitors](property-visitors.html)
  * [Property paths](property-paths.html)
  * [Use `PropertyVisitor` to create a property visitor](property-visitors-PropertyVisitor.html)
  * [Use low-level APIs to create a property visitor](property-visitors-low-level-api.html)

[](properties.html)

Adding functionality to objects at runtime

[](property-visitors.html)

Property visitors

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

