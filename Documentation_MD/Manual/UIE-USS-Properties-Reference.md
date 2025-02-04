[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-Properties-Reference.html)
  * [中文](/cn/current/Manual/UIE-USS-Properties-Reference.html)
  * [日本語](/ja/current/Manual/UIE-USS-Properties-Reference.html)
  * [한국어](/kr/current/Manual/UIE-USS-Properties-Reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-Properties-Reference.html)
  * [中文](/cn/current/Manual/UIE-USS-Properties-Reference.html)
  * [日本語](/ja/current/Manual/UIE-USS-Properties-Reference.html)
  * [한국어](/kr/current/Manual/UIE-USS-Properties-Reference.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS properties](UIE-uss-properties.html)
  * USS properties reference

[](UIE-Transitions.html)

USS transition

[](UIE-uss-color-keywords.html)

USS color keywords

# USS properties reference

The following table lists the USS properties in **UI**(User Interface) Allows
a user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit.

The table indicates which properties are inherited and their
[animatability](UIE-Transitions.html#discrete). For an inherited property, the
element gets the value from its parent element if you don’t specify a value
for it. The following example uses an inherited property to set the font for
all elements.

    
    
    :root {
        -unity-font: resource("Font/consola.ttf");
    }
    

Click the property name to see detailed information about that property.

**Note** : The usage of a USS property that’s the same as the CSS property
links to the Mozilla developer documentation.

**Property** | **Inherited** | **Animatability** | **Description**  
---|---|---|---  
**[`align-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/align-content)** | No | Discrete | Alignment of the whole area of children on the cross axis if they span over multiple lines in this container.  
**[`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)** | No | Discrete | Alignment of children on the cross axis of this container.  
**[`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/align-self)** | No | Discrete | Similar to align-items, but only for this specific element.  
**[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/all)** | No | Fully animatable | Allows resetting all properties with the initial keyword. Does not apply to custom USS properties.  
**[`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)** | No | Fully animatable | Background color to paint in the element’s box.  
**[`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image)** | No | Discrete | Background image to paint in the element’s box.  
**[`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position)** | No | Fully animatable | Background image position value.  
**[`background-position-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position-x)** | No | Discrete | Background image x position value.  
**[`background-position-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position-y)** | No | Discrete | Background image y position value.  
**[`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat)** | No | Discrete | Background image repeat value.  
**[`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-size)** | No | Fully animatable | Background image size value. Transitions are fully supported only when using size in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) or percentages, such as pixel-to-pixel
or percentage-to-percentage transitions.  
**[`border-bottom-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-bottom-color)** | No | Fully animatable | Color of the element’s bottom border.  
**[`border-bottom-left-radius`](UIE-USS-SupportedProperties.html#drawing-borders)** | No | Fully animatable | The radius of the bottom-left corner when a rounded rectangle is drawn in the element’s box.  
**[`border-bottom-right-radius`](UIE-USS-SupportedProperties.html#drawing-borders)** | No | Fully animatable | The radius of the bottom-right corner when a rounded rectangle is drawn in the element’s box.  
**[`border-bottom-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-bottom-width)** | No | Fully animatable | Space reserved for the bottom edge of the border during the layout phase.  
**[`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-color)** | No | Fully animatable | Shorthand for border-top-color, border-right-color, border-bottom-color, border-left-color  
**[`border-left-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-left-color)** | No | Fully animatable | Color of the element’s left border.  
**[`border-left-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-left-width)** | No | Fully animatable | Space reserved for the left edge of the border during the layout phase.  
**[`border-radius`](UIE-USS-SupportedProperties.html#drawing-borders)** | No | Fully animatable | Shorthand for border-top-left-radius, border-top-right-radius, border-bottom-right-radius, border-bottom-left-radius  
**[`border-right-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-right-color)** | No | Fully animatable | Color of the element’s right border.  
**[`border-right-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-right-width)** | No | Fully animatable | Space reserved for the right edge of the border during the layout phase.  
**[`border-top-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-top-color)** | No | Fully animatable | Color of the element’s top border.  
**[`border-top-left-radius`](UIE-USS-SupportedProperties.html#drawing-borders)** | No | Fully animatable | The radius of the top-left corner when a rounded rectangle is drawn in the element’s box.  
**[`border-top-right-radius`](UIE-USS-SupportedProperties.html#drawing-borders)** | No | Fully animatable | The radius of the top-right corner when a rounded rectangle is drawn in the element’s box.  
**[`border-top-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-top-width)** | No | Fully animatable | Space reserved for the top edge of the border during the layout phase.  
**[`border-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/border-width)** | No | Fully animatable | Shorthand for border-top-width, border-right-width, border-bottom-width, border-left-width  
**[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/bottom)** | No | Fully animatable | Bottom distance from the element’s box during layout.  
**[`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/color)** | Yes | Fully animatable | Color to use when drawing the text of an element.  
**[`cursor`](UIE-USS-SupportedProperties.html#cursor)** | No | Non-animatable | Mouse cursor to display when the mouse pointer is over an element.  
**[`display`](UIE-USS-SupportedProperties.html#display)** | No | Discrete | Defines how an element is displayed in the layout.  
**[`flex`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex)** | No | Fully animatable | Shorthand for flex-grow, flex-shrink, flex-basis  
**[`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis)** | No | Fully animatable | Initial main size of a flex item, on the main flex axis. The final layout might be smaller or larger, according to the flex shrinking and growing determined by the other flex properties.  
**[`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction)** | No | Discrete | Direction of the main axis to layout children in a container.  
**[`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-grow)** | No | Fully animatable | Specifies how the item will grow relative to the rest of the flexible items inside the same container.  
**[`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink)** | No | Fully animatable | Specifies how the item will shrink relative to the rest of the flexible items inside the same container.  
**[`flex-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap)** | No | Discrete | Placement of children over multiple lines if not enough space is available in this container.  
**[`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)** | Yes | Fully animatable | Font size to draw the element’s text.  
**[`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/height)** | No | Fully animatable | Fixed height of an element for the layout.  
**[`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)** | No | Discrete | Justification of children on the main axis of this container.  
**[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/left)** | No | Fully animatable | Left distance from the element’s box during layout.  
**[`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing)** | Yes | Fully animatable | Increases or decreases the space between characters.  
**[`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)** | No | Fully animatable | Shorthand for margin-top, margin-right, margin-bottom, margin-left  
**[`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom)** | No | Fully animatable | Space reserved for the bottom edge of the margin during the layout phase.  
**[`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-left)** | No | Fully animatable | Space reserved for the left edge of the margin during the layout phase.  
**[`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-right)** | No | Fully animatable | Space reserved for the right edge of the margin during the layout phase.  
**[`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top)** | No | Fully animatable | Space reserved for the top edge of the margin during the layout phase.  
**[`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/max-height)** | No | Fully animatable | Maximum height for an element, when it is flexible or measures its own size.  
**[`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width)** | No | Fully animatable | Maximum width for an element, when it is flexible or measures its own size.  
**[`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/min-height)** | No | Fully animatable | Minimum height for an element, when it is flexible or measures its own size.  
**[`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/min-width)** | No | Fully animatable | Minimum width for an element, when it is flexible or measures its own size.  
**[`opacity`](UIE-USS-SupportedProperties.html#opacity)** | No | Fully animatable | Specifies the transparency of an element and of its children.  
**[`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow)** | No | Discrete | How a container behaves if its content overflows its own box.  
**[`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)** | No | Fully animatable | Shorthand for padding-top, padding-right, padding-bottom, padding-left  
**[`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-bottom)** | No | Fully animatable | Space reserved for the bottom edge of the padding during the layout phase.  
**[`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-left)** | No | Fully animatable | Space reserved for the left edge of the padding during the layout phase.  
**[`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-right)** | No | Fully animatable | Space reserved for the right edge of the padding during the layout phase.  
**[`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/padding-top)** | No | Fully animatable | Space reserved for the top edge of the padding during the layout phase.  
**[`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position)** | No | Discrete | Element’s positioning in its parent container.  
**[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/right)** | No | Fully animatable | Right distance from the element’s box during layout.  
**[`rotate`](UIE-Transform.html)** | No | Fully animatable | A rotation transformation.  
**[`scale`](UIE-Transform.html)** | No | Fully animatable | A scaling transformation.  
**[`text-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow)** | No | Discrete | The element’s text overflow mode.  
**[`text-shadow`](UIE-USS-SupportedProperties.html#unity-text)** | Yes | Fully animatable | Drop shadow of the text.  
**[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/top)** | No | Fully animatable | Top distance from the element’s box during layout.  
**[`transform-origin`](UIE-Transform.html)** | No | Fully animatable | The transformation origin is the point around which a transformation is applied.  
**[`transition`](UIE-Transitions.html)** | No | Non-animatable | Shorthand for transition-delay, transition-duration, transition-property, transition-timing-function  
**[`transition-delay`](UIE-Transitions.html)** | No | Non-animatable | Duration to wait before starting a property’s transition effect when its value changes.  
**[`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration)** | No | Non-animatable | Time a transition animation should take to complete.  
**[`transition-property`](UIE-Transitions.html)** | No | Non-animatable | Properties to which a transition effect should be applied.  
**[`transition-timing-function`](UIE-Transitions.html)** | No | Non-animatable | Determines how intermediate values are calculated for properties modified by a transition effect.  
**[`translate`](UIE-Transform.html)** | No | Fully animatable | A translate transformation.  
**[`-unity-background-image-tint-color`](UIE-USS-SupportedProperties.html#unity-background)** | No | Fully animatable | Tinting color for the element’s backgroundImage.  
**[`-unity-background-scale-mode`](UIE-USS-SupportedProperties.html#unity-background)** | No | Discrete | Background image scaling in the element’s box.  
**[`-unity-editor-text-rendering-mode`](UIE-USS-SupportedProperties.html#unity-text)** | Yes | Non-animatable | TextElement editor rendering mode.  
**[`-unity-font`](UIE-USS-SupportedProperties.html#unity-font)** | Yes | Discrete | Font to draw the element’s text, defined as a Font object.  
**[`-unity-font-definition`](UIE-USS-SupportedProperties.html#unity-font)** | Yes | Discrete | Font to draw the element’s text, defined as a FontDefinition structure. It takes precedence over `-unity-font`.  
**[`-unity-font-style`](UIE-USS-SupportedProperties.html#unity-font)** | Yes | Discrete | Font style and weight (normal, bold, italic) to draw the element’s text.  
**[`-unity-overflow-clip-box`](UIE-USS-SupportedProperties.html#unity-overflow-clip-box)** | No | Discrete | Specifies which box the element content is clipped against.  
**[`-unity-paragraph-spacing`](UIE-USS-SupportedProperties.html#unity-paragraph-spacing)** | Yes | Fully animatable | Increases or decreases the space between paragraphs.  
**[`-unity-slice-bottom`](UIE-USS-SupportedProperties.html#unity-slice)** | No | Fully animatable | Size of the 9-slice’s bottom edge when painting an element’s background image.  
**[`-unity-slice-left`](UIE-USS-SupportedProperties.html#unity-slice)** | No | Fully animatable | Size of the 9-slice’s left edge when painting an element’s background image.  
**[`-unity-slice-right`](UIE-USS-SupportedProperties.html#unity-slice)** | No | Fully animatable | Size of the 9-slice’s right edge when painting an element’s background image.  
**[`-unity-slice-scale`](UIE-USS-SupportedProperties.html#unity-slice)** | No | Fully animatable | Scale applied to an element’s slices.  
**[`-unity-slice-top`](UIE-USS-SupportedProperties.html#unity-slice)** | No | Fully animatable | Size of the 9-slice’s top edge when painting an element’s background image.  
**[`-unity-text-align`](UIE-USS-SupportedProperties.html#unity-text)** | Yes | Discrete | Horizontal and vertical text alignment in the element’s box.  
**[`-unity-text-generator`](UIE-USS-SupportedProperties.html#unity-text)** | Yes | Non-animatable | Switches between Unity’s standard and advanced text generator  
**[`-unity-text-outline`](UIE-USS-SupportedProperties.html#unity-text)** | No | Fully animatable | Outline width and color of the text.  
**[`-unity-text-outline-color`](UIE-USS-SupportedProperties.html#unity-text)** | Yes | Fully animatable | Outline color of the text.  
**[`-unity-text-outline-width`](UIE-USS-SupportedProperties.html#unity-text)** | Yes | Fully animatable | Outline width of the text.  
**[`-unity-text-overflow-position`](UIE-USS-SupportedProperties.html#unity-text)** | No | Discrete | The element’s text overflow position.  
**[`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility)** | Yes | Discrete | Specifies whether or not an element is visible.  
**[`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space)** | Yes | Discrete | Word wrap over multiple lines if not enough space is available to draw the text of an element.  
**[`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/width)** | No | Fully animatable | Fixed width of an element for the layout.  
**[`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/word-spacing)** | Yes | Fully animatable | Increases or decreases the space between words.  
  
[](UIE-Transitions.html)

USS transition

[](UIE-uss-color-keywords.html)

USS color keywords

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

