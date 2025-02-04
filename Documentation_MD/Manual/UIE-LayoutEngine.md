[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-LayoutEngine.html)
  * [中文](/cn/current/Manual/UIE-LayoutEngine.html)
  * [日本語](/ja/current/Manual/UIE-LayoutEngine.html)
  * [한국어](/kr/current/Manual/UIE-LayoutEngine.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-LayoutEngine.html)
  * [中文](/cn/current/Manual/UIE-LayoutEngine.html)
  * [日本語](/ja/current/Manual/UIE-LayoutEngine.html)
  * [한국어](/kr/current/Manual/UIE-LayoutEngine.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS properties](UIE-uss-properties.html)
  * Position element with the layout engine

[](UIE-USS-SupportedProperties.html)

USS common properties

[](UIE-relative-absolute-positioning-example.html)

Relative and absolute positioning

# Position element with the layout engine

UI Toolkit includes a layout engine that positions elements based on layout
and styling properties. The layout engine uses the layout principles of
[Yoga](https://yogalayout.com/), which implements a subset of
[Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/), a HTML/CSS
layout system. **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit properties match Yoga layout
behavior. UI Toolkit supports most properties in Flexbox.

By default, all elements are part of the layout. The layout has the following
default behaviours:

  * A container distributes its children vertically.
  * The position of a container rectangle includes its children rectangles. This behavior can be limited by other layout properties.
  * A `VisualElement` with text uses the text size in its size calculations. This behavior can be limited by other layout properties.

UI Toolkit includes built-in [controls](UIE-ElementRef.html#built-in-controls)
for standard UI components, such as a button, toggle, or text field. These
built-in controls have styles that affect their layout.

## Main style properties

The following are the main style properties:

  * **Flex > Direction** (`flex-direction` in USS): Defines the layout direction the **main-axis**. The default is `column` and that makes the **main-axis** run from top to bottom.
  * **Flex > Grow** (`flex-grow` in USS): Defines how an element should grow in the **main-axis**. It’s a ratio that’s shared with all other siblings of the same parent. This property is useful when trying make an element stretch to take up the entire size of its parents (minus any siblings). To do this, set the **Flex > Grow** value to `1`. If you have two siblings with `flex-grow` set to `1`, they will each take 50% of the parent’s available size along the **main-axis**.
  * **Align > Align Items** (`align-items` in USS): Defines the alignment of elements in the **cross-axis** , or the perpendicular axis to the **main-axis**. For example, if you have two Buttons in a `VisualElement` that has `flex-direction: column` and `align-items: flex-end` set, the two Buttons will squish against the container’s right edge. The options for `align-items` have names like `flex-start` and `flex-end` because they depend on the value of `flex-direction`.
  * **Align > Justify Content** (`justify-content` in USS): Defines the alignment of elements in the **main-axis**. For example, if you have two Buttons in a `VisualElement` that has `flex-direction: column` and `justify-content: flex-end` set, the two Buttons squish against the container’s bottom edge. The options for `justify-content` are named like `flex-start` and `flex-end` because they depend on the value of `flex-direction`.

For more information, refer to [Flex layout](UIE-USS-
SupportedProperties.html#flex-layout).

If the selected element has child elements, in UI Builder, you can use toggles
in the header to toggle flex-related style properties in the ****Viewport**
The user’s visible area of an app on their screen.  
See in [Glossary](Glossary.html#Viewport)**. The image below shows the options
available for the `#menu` element:

![FlexPropertiesInCanvas](../uploads/Main/UIBuilder/FlexPropertiesInCanvas.png)
FlexPropertiesInCanvas

You can use the style properties to create complex, dynamic layouts. Here’s an
example of a layout that anchors a `Button` on the bottom-right edge of the
screen:

![BottomRightCornerButtonLayout](../uploads/Main/UIBuilder/BottomRightCornerButtonLayout.png)
BottomRightCornerButtonLayout

The UXML for this layout, showing the inline styles set on each container
`VisualElement`, is below:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <ui:VisualElement name="screen-is-blue" style="flex-grow: 1; justify-content: flex-end; background-color: blue;">
            <ui:VisualElement name="toolbar-is-orange" style="align-items: flex-end; background-color: orange;">
                <ui:Button text="Button" display-tooltip-when-elided="true" />
            </ui:VisualElement>
        </ui:VisualElement>
    </ui:UXML>
    

The containers are colored to reveal their shape. You can use nested
`VisualElement` containers to achieve any dynamic layout without resorting to
explicitly setting the position and size of each element. This keeps the
layout dynamic and automatically adjusts to the larger container changing
size, like the screen changing size.

## Absolute position

UI Builder also supports the **Position** style properties. The **Position >
Absolute** mode makes an element invisible to the default Flexbox-based layout
engine. It’s as if it no longer takes any space. **Absolute** -position
elements appear on top of any siblings that are **Relative** -position.

While using **Absolute** position, you can use the **Position > Left**,
**Top** , **Right** , **Bottom** style properties to offset and size the
element from the respective edges of its parent. This doesn’t set absolute
coordinates on the screen but sets offsets relative to the parent element. You
can still use **Relative** mode to position the parent element. If you set
both a **Left** offset and a **Right** offset, the **Width** style property of
the element is ignored and the computed width will now come from the following
formula:

    
    
    element-computed-width = parent-width - left-offset - right-offset
    

**Left** , **Top** , **Right** , **Bottom** can also be interpreted as
anchors. For example, you can anchor a `Button` on the bottom-left of the
screen:

![Anchoring Example](../uploads/Main/uie-anchoring-example.png) Anchoring
Example

The UXML below displays the inline styles:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements" editor-extension-mode="False">
        <ui:VisualElement style="flex-grow: 1;">
            <ui:VisualElement style="position: absolute; left: 0; bottom: 0;" />
        </ui:VisualElement>
    </ui:UXML>
    

With positioning, there is a difference between having **Left** set to `0` and
having **Left** unset:

  * `Left set to 0` means set an offset of 0.
  * `Left unset` doesn’t set any offset and lets other style properties define the width or height of the element.

You can also modify these offset style properties directly in the **Canvas**
via additional resize handles on each edge and corner of the element’s blue
selection border. It’s important to differentiate between what’s set and
what’s unset, so the **Canvas** also includes “anchor” toggles as orange
squares off each side of the element. The **Canvas** handles will adjust which
style properties are set when resizing the element visually, depending on
which “anchors” are set. For example, say you are resizing the element in the
**Canvas** via its right-border handle:

  * If you set both **Left** and **Right** properties, the handle will update the **Right** property.
  * If you set **Left** but not **Right** , the handle will update the **Width** property.

## Use both Relative and Absolute

Avoid to use **Absolute** position mode because it bypasses the built-in
layout engine in UI Toolkit and can lead to high-maintenance UI where changing
the overall layout requires manually updating individual elements. However,
**Absolute** positioning is appropriate for specific use cases, such as
overlays. It’s useful to overlay some complex UI on top of other complex UI,
such as a popup or a dropdown. In these cases, use **Absolute** position for
the overlay container, but continue using **Relative** mode for elements
inside the overlay to maintain flexibility.

The following shows an example of a simple centered popup:

![AbsolutePositionOverlayWithPopup](../uploads/Main/UIBuilder/AbsolutePositionOverlayWithPopup.png)
And here’s the UXML for your reference:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <ui:VisualElement name="complex-ui-screen">
            <ui:Toggle label="Toggle" />
            <ui:MinMaxSlider picking-mode="Ignore" label="Min/Max Slider" min-value="10" max-value="12" low-limit="-10" high-limit="40" />
            <ui:Label text="Label" />
            <ui:Button text="Button" />
            <ui:Button text="Button" />
        </ui:VisualElement>
        <ui:VisualElement name="overlay" style="position: absolute; left: 0; top: 0; right: 0; bottom: 0; background-color: rgba(0, 0, 0, 0.71); align-items: center; justify-content: center;">
            <ui:VisualElement name="popup" style="background-color: rgba(70, 70, 70, 255);">
                <ui:Label text="Exit?" name="message" />
                <ui:Button text="OK" name="ok-button" style="width: 108.3333px;" />
            </ui:VisualElement>
        </ui:VisualElement>
    </ui:UXML>
    

The example above highlights the use of **Absolute** position. Set all
**Position > Left**, **Top** , **Right** , **Bottom** to `0`, so the position
is `0` pixels away from the edges of the screen. This makes the `#overlay`
element overlap the `#complex-ui-screen` container element. You can also set a
semi-transparent background to the `#overlay` element to make the other UI
appear darkened. Use `#overlay` to set **Relative** position to center our
`#popup` container `VisualElement`.

## Best practices

The following list provides tips to help improve the performance of the layout
engine:

  * Set the `width` and `height` to define the size of an element.

  * Use the `flexGrow` property ([USS](UIE-USS.html): `flex-grow: <value>;`) to assign a flexible size to an element. The value of the `flexGrow` property assigns a base weight to the size of an element when it’s determined by its siblings.

  * Set the `flexDirection` property to `row` ([USS](UIE-USS.html): `flex-direction: row;`) to switch to a horizontal layout.

  * Use relative positioning to offset an element based on its original layout position.

  * Set the `position` property to `absolute` to place an element relative to its parent position rectangle. This doesn’t affect the layout of its siblings or parent.

## Additional resources

  * [USS properties reference](UIE-USS-Properties-Reference.html)
  * [USS common properties](UIE-USS-SupportedProperties.html)
  * [Style UI with USS](UIE-USS.html)
  * [Relative and absolute positioning C# example](UIE-relative-absolute-positioning-example.html)

[](UIE-USS-SupportedProperties.html)

USS common properties

[](UIE-relative-absolute-positioning-example.html)

Relative and absolute positioning

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

