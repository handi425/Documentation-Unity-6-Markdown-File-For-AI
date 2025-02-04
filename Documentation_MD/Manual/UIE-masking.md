[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-masking.html)
  * [中文](/cn/current/Manual/UIE-masking.html)
  * [日本語](/ja/current/Manual/UIE-masking.html)
  * [한국어](/kr/current/Manual/UIE-masking.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-masking.html)
  * [中文](/cn/current/Manual/UIE-masking.html)
  * [日本語](/ja/current/Manual/UIE-masking.html)
  * [한국어](/kr/current/Manual/UIE-masking.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * Apply masking effects in UI Toolkit

[](UIE-tss.html)

Theme Style Sheet (TSS)

[](UIE-ui-debugger.html)

UI Toolkit Debugger

# Apply masking effects in UI Toolkit

Masking is a technique that lets you control which parts of a **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) element are visible. In UI Toolkit, you
can use USS property `overflow: hidden` to hide parts of a UI element that are
outside the bounds of another UI element.

## Masking with an element

You can use an element to mask another element. To make a masking effect with
an element, add the masking element as the parent element of the masked
element. Set the `overflow` property to `hidden` on the masking element. This
hides the parts of the masked element that are outside the bounds of the
masking element.

The following example shows how to make a masking effect with a rectangle
shape and a rounded corner shape.

![Making examples with and without rounded
corners](../uploads/Main/uitk/masks.gif) Making examples with and without
rounded corners

In the example, the `#MaskSquare` and `MaskRounded` elements are the masking
elements, and the `Logo1` and `Logo2` elements are the masked elements. The
masking elements are the parent elements of the masked elements. The example
uses a `VisualElement` with a background image to demonstrate the masking
effect. You can apply the masking technique to any element, such as a Label or
a Button.

The `#MaskRounded` element has a `border-radius` property set to `50px`. This
creates a rounded corner masking effect.

The UXML looks like this:

    
    
    <UXML>
        <VisualElement name="MaskSquare" >
            <VisualElement name="Logo1" />
        </VisualElement>
        <VisualElement name="MaskRounded" >
            <VisualElement name="Logo2"  />
        </VisualElement>
    </UXML>
    

The USS looks like this:

    
    
    #MaskSquare {
        overflow: hidden;
    }
    
    #MaskRounded {
        overflow: hidden;
        border-radius: 50px;
    }
    
    #Logo1, #Logo2 {
        background-image: url("unity-logo.png");
    }
    

## Masking with arbitrary shapes

To make a masking effect with an arbitrary shape, set an SVG as the background
image of the masking element as shown below:

![A masking example with SVG](../uploads/Main/uitk/masks-svg.gif) A masking
example with SVG

The UXML looks like this:

    
    
    <UXML>
        <VisualElement name="MaskSVG" >
            <VisualElement name="Logo3" />
        </VisualElement>
    </UXML>
    

The USS looks like this:

    
    
    #MaskSVG {
        overflow: hidden;
        background-image: url("mask.svg");
    }   
    
    #Logo3 {
        background-image: url("unity-logo.png");
    }
    

## Reduce batch breaks for nested masking

Nested masking occurs when both an element and one or more ancestors define a
mask. The intersection of these masks defines the final visibility. You can
use this technique to create intricate visual effects or selectively reveal
parts of an image based on various criteria. For example, you can define masks
to display certain regions of an element and hide other masked areas.

When masking with rectangle shapes, Unity uses axis-aligned rectangles as the
clipping region, this is called rectangle clipping. When masking with rounded
corners or arbitrary shapes, Unity uses stencil masking instead of rectangle
clipping. Stencil masking stores masks in a stencil, which is a special image
type with 8 bits per channel. The shape stored in the stencil defines the
clipping region. For more information, refer to [ShaderLab command:
Stencil](SL-Stencil.html).

Stencil masking uses a GPU feature called a **stencil buffer** A memory store
that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to
flag pixels, and then only render to pixels that pass the stencil operation.
[More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#stencilbuffer) for masking operations. The
stencil has a GPU-associated state that dictates image modification and its
impact on rendering. When elements share the same stencil state, they can be
batched into a single draw call. However, any change in the stencil state,
such as nested masking, results in batching breaking. Batch breaking can
significantly impact performance as it prevents multiple elements from being
efficiently rendered together in a single draw call. It’s crucial to minimize
batch breaking to optimize rendering performance.

To reduce the number of batch breaks for nested stencil masking, consider
applying
[`UsageHints.MaskContainer`](../ScriptReference/UIElements.UsageHints.MaskContainer.html)
on the masking element that’s the ancestor of all the masks.

The following illustration shows the number of batches in a single-level
masking, a nested masking, and a nested masking with `MaskContainer` applied.
The yellow color indicates the masking elements. The orange color indicates
the masking element with `MaskContainer` applied. The numbers indicate the
number of batches.

![Batch breaking example](../StaticFiles/ScriptRefImages/MaskContainer.png)
Batch breaking example

A: Single-level masking (1 batch)  
B: Nested masking (5 batches)  
C: Nested masking with MaskContainer (2 batches)

## Additional resources

  * [UsageHints](../ScriptReference/UIElements.UsageHints.html)
  * [Appearance](UIE-USS-SupportedProperties.html#unity-overflow-clip-box)

[](UIE-tss.html)

Theme Style Sheet (TSS)

[](UIE-ui-debugger.html)

UI Toolkit Debugger

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

