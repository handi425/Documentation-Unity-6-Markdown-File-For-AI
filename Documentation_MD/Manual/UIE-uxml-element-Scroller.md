[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-uxml-element-Scroller.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-Scroller.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-Scroller.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-Scroller.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-uxml-element-Scroller.html)
  * [中文](/cn/current/Manual/UIE-uxml-element-Scroller.html)
  * [日本語](/ja/current/Manual/UIE-uxml-element-Scroller.html)
  * [한국어](/kr/current/Manual/UIE-uxml-element-Scroller.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Visual elements reference](UIE-ElementRef.html)
  * Scroller

[](UIE-uxml-element-ScrollView.html)

ScrollView

[](UIE-uxml-element-Slider.html)

Slider

# Scroller

A Scroller lets users scroll through content in your user interface.

## Create a Scroller

You can create a Scroller with **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, UXML, or C#. The following C#
example creates a Scroller with a default value, low limit, and high limit,
and sets the direction of the Scroller:

    
    
    var scroller = new Scroller();
    scroller.value = 42;
    scroller.lowValue = 0;
    scroller.highValue = 100;
    scroller.direction = SliderDirection.Vertical;
    

## Example

The following UXML example creates a Scroller:

    
    
    <UXML xmlns="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <Scroller
            name="the-uxml-scroller"
            direction="Horizontal"
            low-value="0"
            high-value="100" />
    </UXML>
    

The following C# example illustrates some of the customizable functionalities
of the Scroller:

    
    
    /// <sample>
    // Get a reference to the scroller from UXML and assign it its value.
    var uxmlField = container.Q<Scroller>("the-uxml-scroller");
    uxmlField.valueChanged += (v) => {};
    uxmlField.value = 42;
    
    // Create a new scroller, disable it, and give it a style class.
    var csharpField = new Scroller(0, 100, (v) => {}, SliderDirection.Vertical);
    csharpField.SetEnabled(false);
    csharpField.AddToClassList("some-styled-scroller");
    csharpField.value = uxmlField.value;
    container.Add(csharpField);
    
    // Mirror value of uxml scroller into the C# field.
    uxmlField.RegisterCallback<ChangeEvent<float>>((evt) =>
    {
        csharpField.value = evt.newValue;
    });
    /// </sample>
    

To try this example live in Unity, go to **Window** > **UI Toolkit** >
**Samples**.

## C# base class and namespace

**C# class** : [`Scroller`](../ScriptReference/UIElements.Scroller.html)  
**Namespace** : `UnityEngine.UIElements`  
**Base class** :
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html)

## Member UXML attributes

This element has the following member attributes:

**Name** | **Type** | **Description**  
---|---|---  
`direction` | [`UIElements.SliderDirection`](../ScriptReference/UIElements.SliderDirection.html) | Direction of this scrollbar.  
`high-value` | `float` | Maximum value.  
`low-value` | `float` | Minimum value.  
`value` | `float` | Value that defines the slider position. It lies between `lowValue` and `highValue`.  
  
## Inherited UXML attributes

This element inherits the following attributes from its base class:

**Name** | **Type** | **Description**  
---|---|---  
`focusable` | `boolean` | True if the element can be focused.  
`tabindex` | `int` | An integer used to sort focusables in the focus ring. Must be greater than or equal to zero.  
  
This element also inherits the following attributes from
[`VisualElement`](UIE-uxml-element-VisualElement.html):

**Name** | **Type** | **Description**  
---|---|---  
`content-container` | `string` | Child elements are added to it, usually this is the same as the element itself.  
`data-source` | `Object` | Assigns a data source to this VisualElement which overrides any inherited data source. This data source is inherited by all children.  
`data-source-path` | `string` | Path from the data source to the value.  
`data-source-type` | `System.Type` | The possible type of data source assignable to this VisualElement.  
  
This information is only used by the UI Builder as a hint to provide some
completion to the data source path field when the effective data source cannot
be specified at design time.  
`language-direction` | [`UIElements.LanguageDirection`](../ScriptReference/UIElements.LanguageDirection.html) | Indicates the directionality of the element’s text. The value will propagate to the element’s children.  
  
Setting the languageDirection to RTL adds basic support for right-to-left
(RTL) by reversing the text and handling linebreaking and word wrapping
appropriately. However, it does not provide comprehensive RTL support, as this
would require text shaping, which includes the reordering of characters, and
OpenType font feature support. Comprehensive RTL support is planned for future
updates, which will involve additional APIs to handle language, script, and
font feature specifications.  
  
To enhance the RTL functionality of this property, users can explore available
third-party plugins in the Unity Asset Store and make use of
`ITextElementExperimentalFeatures.renderedText`  
`name` | `string` | The name of this VisualElement.  
  
Use this property to write USS selectors that target a specific element. The
standard practice is to give an element a unique name.  
`picking-mode` | [`UIElements.PickingMode`](../ScriptReference/UIElements.PickingMode.html) | Determines if this element can be pick during mouseEvents or `IPanel.Pick` queries.  
`style` | `string` | Sets the `VisualElement` style values.  
`tooltip` | `string` | Text to display inside an information box after the user hovers the element for a small amount of time. This is only supported in the Editor UI.  
`usage-hints` | [`UIElements.UsageHints`](../ScriptReference/UIElements.UsageHints.html) | A combination of hint values that specify high-level intended usage patterns for the `VisualElement`. This property can only be set when the `VisualElement` is not yet part of a `Panel`. Once part of a `Panel`, this property becomes effectively read-only, and attempts to change it will throw an exception. The specification of proper `UsageHints` drives the system to make better decisions on how to process or accelerate certain operations based on the anticipated usage pattern. Note that those hints do not affect behavioral or visual results, but only affect the overall performance of the panel and the elements within. It’s advised to always consider specifying the proper `UsageHints`, but keep in mind that some `UsageHints` might be internally ignored under certain conditions (e.g. due to hardware limitations on the target platform).  
`view-data-key` | `string` | Used for view data persistence, such as tree expanded states, scroll position, or zoom level.  
  
This key is used to save and load the view data from the view data store. If
you don’t set this key, the persistence is disabled for the associated
`VisualElement`. For more information, refer to [View data persistence](UIE-
ViewData.html).  
  
## USS classes

The following table lists all the C# public property names and their related
USS selector.

**C# property** | **USS selector** | **Description**  
---|---|---  
`ussClassName` | `.unity-scroller` | USS class name of elements of this type.  
`horizontalVariantUssClassName` | `.unity-scroller--horizontal` | USS class name of elements of this type, when they are displayed horizontally.  
`verticalVariantUssClassName` | `.unity-scroller--vertical` | USS class name of elements of this type, when they are displayed vertically.  
`sliderUssClassName` | `.unity-scroller__slider` | USS class name of slider elements in elements of this type.  
`lowButtonUssClassName` | `.unity-scroller__low-button` | USS class name of low buttons in elements of this type.  
`highButtonUssClassName` | `.unity-scroller__high-button` | USS class name of high buttons in elements of this type.  
`disabledUssClassName` | `.unity-disabled` | USS class name of local disabled elements.  
  
You can also use the [Matching Selectors section in the Inspector or the UI
Toolkit Debugger](UIB-testing-ui.html#matching-selectors) to see which USS
selectors affect the components of the `VisualElement` at every level of its
hierarchy.

## Additional resources

  * [ScrollView](UIE-uxml-element-ScrollView.html)A UI Control which displays a large set of Controls in a viewable area that you can see by using a scrollbar. [More info](UIE-uxml-element-ScrollView.html)  
See in [Glossary](Glossary.html#ScrollView)

[](UIE-uxml-element-ScrollView.html)

ScrollView

[](UIE-uxml-element-Slider.html)

Slider

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

