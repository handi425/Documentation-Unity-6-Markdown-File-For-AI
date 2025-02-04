[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/property-visitors.html)
  * [中文](/cn/current/Manual/property-visitors.html)
  * [日本語](/ja/current/Manual/property-visitors.html)
  * [한국어](/kr/current/Manual/property-visitors.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/property-visitors.html)
  * [中文](/cn/current/Manual/property-visitors.html)
  * [日本語](/ja/current/Manual/property-visitors.html)
  * [한국어](/kr/current/Manual/property-visitors.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Adding functionality to objects at runtime](properties.html)
  * Property visitors

[](property-bags.html)

Property bags

[](property-paths.html)

Property paths

# Property visitors

Property visitors are algorithms built on top of the Properties API.

## Concept

You can use visitors to add functionality to types without the need for direct
modifications. You can create highly generic visitors to control both the
algorithm itself and the visitation process. This differs from the classic
implementation of the visitor pattern, where the visitation typically occurs
on a known ahead-of-time type structure. It enables features like
[serialization](https://docs.unity3d.com/Packages/com.unity.serialization@3.1/manual/index.html),
inspector-like **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) generation, among others.

The following is the basic pattern of visitors. It takes place on the property
bags and property companion objects.

  1. An instance of a type **accepts** a visitor.
  2. The visitor **visits** the the property bag of the instance.
  3. The property bag can loop through its properties and **accept** the visitor.

## Create a property visitor to get properties

You can use the following approaches to create your visitors to get
properties:

  * Use the [`Unity.Properties.PropertyVisitor`](../ScriptReference/Unity.Properties.PropertyVisitor.html) base class. Refer to [Use `PropertyVisitor` to create a property visitor](property-visitors-PropertyVisitor.html) for an example.
  * Implement the [`IPropertyBagVisitor`](../ScriptReference/Unity.Properties.IPropertyBagVisitor.html) and [`IPropertyVisitor`](../ScriptReference/Unity.Properties.IPropertyVisitor.html) interfaces. Refer to [Use low-level APIs to create a property visitor](property-visitors-low-level-api.html) for an example.

The first approach is the easiest way to get started. However, for more
extensive customization of the visitation behavior for both the property bags
and the properties, use the second approach, which offers greater flexibility
and the potential for performance improvements.

The following example uses the
[`PropertyVisitor`](../ScriptReference/Unity.Properties.PropertyVisitor.html)
class to create a simple visitor that gets the properties of a given type that
are tagged with a certain attribute:

    
    
    public class BindableAttribute
        : Attribute
    {
    }
    
    public class GatherBindablePropertiesVisitor
        : PropertyVisitor
    {
        public List<PropertyPath> BindableProperties { get; set; }
    
        protected override void VisitProperty<TContainer, TValue>(Property<TContainer, TValue> property, ref TContainer container, ref TValue value)
        {
            if (property.HasAttribute<BindableAttribute>())
                BindableProperties.Add(PropertyPath.AppendProperty(default, property));
        }
    }
    

The following is the equivalent example that uses the `IPropertyBagVisitor`
interface to create the visitor:

    
    
    public class BindableAttribute
        : Attribute
    {
    }
    
    public class GatherBindablePropertiesVisitor
        : IPropertyBagVisitor
    {
        public List<PropertyPath> BindableProperties { get; set; }
    
        void IPropertyBagVisitor.Visit<TContainer>(IPropertyBag<TContainer> propertyBag, ref TContainer container)
        {
            // Loop through the properties of the container object.
            foreach (var property in propertyBag.GetProperties(ref container))
            {
                if (property.HasAttribute<BindableAttribute>())
                    BindableProperties.Add(PropertyPath.AppendProperty(default, property));
            }
        }
    }
    

The low-level visitor is more performant because it doesn’t need to loop
through all the properties of the property bag and extract their value. You
can also use low-level visitors to visit properties that aren’t part of a
property bag.

## Performance considerations

Property bags, properties and visitors are all implemented using generic types
so that we can remain as strongly-typed as possible and, in many cases, avoid
boxing allocations during visitation. The trade-off of using generic types is
that the JIT compiler will generate the IL for a given method the first time
it is called. This can result in a slower execution the first time a visitor
is accepted on an object.

## Additional resources

  * [Property bags](property-bags.html)
  * [Property paths](property-paths.html)
  * [Use `PropertyVisitor` to create a property visitor](property-visitors-PropertyVisitor.html)
  * [Use low-level APIs to create a property visitor](property-visitors-low-level-api.html)

[](property-bags.html)

Property bags

[](property-paths.html)

Property paths

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

