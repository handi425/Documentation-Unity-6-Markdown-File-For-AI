[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-runtime-binding-types.html)
  * [中文](/cn/current/Manual/UIE-runtime-binding-types.html)
  * [日本語](/ja/current/Manual/UIE-runtime-binding-types.html)
  * [한국어](/kr/current/Manual/UIE-runtime-binding-types.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-runtime-binding-types.html)
  * [中文](/cn/current/Manual/UIE-runtime-binding-types.html)
  * [日本語](/ja/current/Manual/UIE-runtime-binding-types.html)
  * [한국어](/kr/current/Manual/UIE-runtime-binding-types.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [Runtime data binding](UIE-runtime-binding.html)
  * Create a runtime binding in C# scripts

[](UIE-get-started-runtime-binding.html)

Get started with runtime binding

[](UIE-runtime-binding-define-data-source.html)

Define a data source for runtime binding

# Create a runtime binding in C# scripts

To bind a property of a **visual element** A node of a visual tree that
instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) to a data source in C#, create
an instance of
[`DataBinding`](../ScriptReference/UIElements.DataBinding.html). With this
binding type, you can define a
[`dataSource`](../ScriptReference/UIElements.DataBinding-dataSource.html) and
a [`dataSourcePath`](../ScriptReference/UIElements.DataBinding-
dataSourcePath.html) directly on the binding instance.

## Basic workflow

To create a runtime binding in C#, follow these steps:

  1. Create a binding. Bindings are objects that you can create, register, or unregister to a visual element through a unique ID.
  2. [Define the data source](UIE-runtime-binding-define-data-source.html) and the data source path for the binding object. The data source is the object that contains the property you want to bind to. The data source path is a relative path from the data source to the property you want to bind to.
  3. [Define the binding mode and update triggers](UIE-runtime-binding-mode-update.html) for the binding object. The binding mode defines how changes are replicated between the data source and the **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI). The update trigger defines when to update
the binding object.

  4. Register the binding object to the visual element.
  5. If necessary, [add type converters to convert data types between the data source and the UI](UIE-runtime-binding-data-type-conversion.html).

The following example created a binding object and registers it to a visual
element.

    
    
    var dataSource = ScriptableObject.CreateInstance<ExampleObject>();
    
    var root = new VisualElement
    {
        name = "root",
        dataSource = dataSource
    };
    
    var vector3Field = new Vector3Field("Vec3 Field");
    
    vector3Field.SetBinding("label", new DataBinding
    {
        dataSourcePath = new PropertyPath(nameof(ExampleObject.vector3Label)),
        bindingMode = BindingMode.ToTarget
    });
    
    vector3Field.SetBinding("value", new DataBinding
    {
        dataSourcePath = new PropertyPath(nameof(ExampleObject.vector3Value))
    });
    
    root.Add(vector3Field);
    
    var floatField = new FloatField("Float Field") { value = 42.2f };
    
    floatField.SetBinding("value", new DataBinding
    {
        dataSourcePath = new PropertyPath(nameof(ExampleObject.sumOfVector3Properties))
    });
    
    root.Add(floatField);
    
    var label = new Label("Label")
    {
        dataSourcePath = new PropertyPath(nameof(ExampleObject.dangerLevel))
    };
    
    // Here, we do not need to set the dataSourcePath because we will only use two bindings and they will use the same path,
    // so we set the dataSourcePath on the Label directly instead.
    var binding = new DataBinding
    {
        bindingMode = BindingMode.ToTarget
    };
    
    // Add a custom float -> string converter
    binding.sourceToUiConverters.AddConverter((ref float v) => 
    {
        return v switch
        {
            >= 0 and < 1.0f/3.0f => "Danger",
            >= 1.0f/3.0f and < 2.0f/3.0f => "Neutral",
            _ => "Good"
        };
    });
    
    // Add a custom float -> StyleColor
    binding.sourceToUiConverters.AddConverter((ref float v) => new StyleColor(Color.Lerp(Color.red, Color.green, v)));
    
    // Since the binding is targeting the same data source property, we can reuse the same instance.
    label.SetBinding("text", binding);
    label.SetBinding("style.backgroundColor", binding);
    
    root.Add(label);
    

It’s equivalent to the following UXML:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" xsi="http://www.w3.org/2001/XMLSchema-instance" engine="UnityEngine.UIElements" 
    editor="UnityEditor.UIElements" noNamespaceSchemaLocation="../UIElementsSchema/UIElements.xsd" editor-extension-mode="False">
        <ui:VisualElement data-source="ExampleObject.asset" name="VisualElement" >
            <ui:Vector3Field label="Vec3 Field">
                <Bindings>
                    <ui:DataBinding property="label" data-source-path="vector3Label" binding-mode="ToSource" />
                    <ui:DataBinding property="value" data-source-path="vector3Value" />
                </Bindings>
            </ui:Vector3Field>
            <ui:FloatField label="Float Field" value="42.2">
                <Bindings>
                    <ui:DataBinding property="value" data-source-path="sumOfVector3Properties" binding-mode="ToTarget" />
                </Bindings>
            </ui:FloatField>
            <ui:Label text="Label" data-source-path="dangerLevel">
                <Bindings>
                    <ui:DataBinding property="text" binding-mode="ToTarget" source-to-ui-converters="Value To Progress" />
                    <ui:DataBinding property="style.backgroundColor" binding-mode="ToTarget" source-to-ui-converters="Value To Progress" />
                </Bindings>
        </ui:Label>
        </ui:VisualElement>
    </ui:UXML>
    

## Register and unregister binding objects

You can use the following methods to manage binding objects:

  * [`SetBinding`](../ScriptReference/UIElements.VisualElement.SetBinding.html)
  * [`GetBinding`](../ScriptReference/UIElements.VisualElement.GetBinding.html)
  * [`TryGetBinding`](../ScriptReference/UIElements.VisualElement.TryGetBinding.html)
  * [`GetBindingInfos`](../ScriptReference/UIElements.VisualElement.GetBindingInfos.html)
  * [`HasBinding`](../ScriptReference/UIElements.VisualElement.HasBinding.html)
  * [`ClearBinding`](../ScriptReference/UIElements.VisualElement.ClearBinding.html)
  * [`ClearBindings`](../ScriptReference/UIElements.VisualElement.ClearBindings.html)

## Report a change

You can create the bindable properties in the same way as other data sources,
which means that you can also use `VisualElement` types as [data sources](UIE-
runtime-binding-define-data-source.html). The main difference between a
`VisualElement` type and other data sources is that `VisualElement` types come
with built-in versioning. You must use the built-in versioning of a
`VisualElement` type to propagate changes.

To report a change, call the
[`NotifyPropertyChanged`](../ScriptReference/UIElements.CallbackEventHandler.NotifyPropertyChanged.html)
method. This method takes a
[`BindingId`](../ScriptReference/UIElements.BindingId.html) that identifies
the property that changed.

The following example shows how to report a change for a `VisualElement` type:

    
    
    // Creates a static readonly BindingId that is unique to this type. This is used to identify the property. 
    public static readonly BindingId intValueProperty = nameof(intValue);
    
    private int m_IntValue;
    
    [CreateProperty]
    public int intValue
    {
        get => m_IntValue;
        set
        {
            if (m_IntValue == value)
                return;
            m_IntValue = value;
            
            // This instructs the binding system that a change occured.
            NotifyPropertyChanged(intValueProperty);
        }
    }
    

## Best practices

Follow these tips and best practices to optimize performance:

  * **Use correct binding IDs** : The binding system uses the binding ID to identify the binding object and the target property of the element. The binding ID must be the target property of the element. For example, if you want to bind to the `value` property of a `Vector3Field`, the binding ID must be `Vector3Field.valueProperty`.
  * **Avoid internal data updates with bindings** : Don’t use bindings to update the internal data of a visual element. For example, don’t use bindings to synchronize the `x`, `y`, and `z` sub-elements for a `Vector3Field`. Instead, use a binding to synchronize the `value` property of the `Vector3Field` with a `Vector3` property of a data source.

## Known limitations

UI Toolkit doesn’t report changes in `element.style` and
`element.resolvedStyle`. Therefore, you can use binding instances to target
the resolved style of an element but can’t track changes to them.

## Additional resources

  * [Runtime data binding](UIE-runtime-binding.html)
  * [Create custom binding types](UIE-runtime-binding-custom-types.html)
  * [Define logging levels](UIE-runtime-binding-logging-levels.html)

[](UIE-get-started-runtime-binding.html)

Get started with runtime binding

[](UIE-runtime-binding-define-data-source.html)

Define a data source for runtime binding

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

