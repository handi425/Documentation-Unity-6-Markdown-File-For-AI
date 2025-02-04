[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Transform.html)
  * [中文](/cn/current/Manual/UIE-Transform.html)
  * [日本語](/ja/current/Manual/UIE-Transform.html)
  * [한국어](/kr/current/Manual/UIE-Transform.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Transform.html)
  * [中文](/cn/current/Manual/UIE-Transform.html)
  * [日本語](/ja/current/Manual/UIE-Transform.html)
  * [한국어](/kr/current/Manual/UIE-Transform.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS properties](UIE-uss-properties.html)
  * USS transform

[](UIE-image-import-settings.html)

Image import settings

[](UIE-Transitions.html)

USS transition

# USS transform

The transform properties apply a 2D transformation to a **visual element** A
node of a visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). You can use them to rotate,
scale, or move a visual element.

If you change the layout of an element, Unity recalculates the layout of other
elements in the same hierarchy. This recalculation might reduce an animation’s
frame rate. Applying transform to an element reduces recalculations because it
doesn’t change the layout of other elements in the hierarchy.

It’s possible to use transform to define the static appearance of a visual
element. However, transform is best used for changes and animations. For
example, if you want to make a visual element shake when an event happens in
an application, set the position of the visual element using the regular
layout properties such as `top` and `left`, and then use `translate` to align
an offset relative to the initial position.

Transform includes the following properties:

**Property** | **USS syntax** | **Description**  
---|---|---  
**Transform Origin** | `transform-origin` | Represents the point of origin where rotation, scaling, and translation occur.  
**Translate** | `translate` | Repositions the visual element in horizontal or vertical directions.  
**Scale** | `scale` | Changes the apparent size, padding, border, and margins of a visual element. Negative values flip visual elements along the scale axis.  
**Rotate** | `rotate` | Rotates a visual element. Positive values represent clockwise rotation and negative values represent counterclockwise rotation. You can set rotation with `deg`, `grad`, `rad`, or `turn` units. For more information on these units, see [MDN Web Docs’s page on the `<angle>` CSS data type](https://developer.mozilla.org/en-US/docs/Web/CSS/angle).  
  
**Note** : All transformations are performed in the following order:

  1. Scale
  2. Rotate
  3. Translate

You can set transform properties for a visual element using the controls in
the [UI Builder](UIBuilder.html), within a [USS](UIE-USS.html) file, or using
a C# script.

## Transform controls in the UI Builder

You can use the controls in the **Transform** section of the ****Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** in the **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder to set the transform properties of
a visual element.

### Pivot Origin

The **Pivot Origin** widget sets the transform origin property. To use it, do
one of the following:

  * Click a point in the widget to set the origin to a corner, the center of an edge, or the center. You can also define the values using the keyboard. When the widget is in focus, use the arrow keys to specify a point in the widget.
  * Enter values for **X** and **Y** and specify the unit.

**Tip** : You can enter `%` or `px` after values. This automatically changes
the displayed unit in the unit selector. You can also drag to define the
values in the **X** and **Y** boxes.

**Note** : The default value for the transform origin is center.

If you use percentages for both the X and Y values, the widget shows the new
origin point when you edit the X and Y text boxes.

If you specify a transform origin point outside the element, such as having a
value less than 0% or greater than 100%, the widget shows the directions of
the X and Y axes.

![](../uploads/Main/TransformOriginWgt.png)

### Translate

The **Translate** control sets the translate property. To use it, enter values
in the **X** and **Y** boxes and specify the unit.

**Tip** : You can enter `%` or `px` after values. This automatically changes
the displayed unit in the unit selector. You can also drag to define the
values in the **X** and **Y** boxes.

### Scale

The **Scale** control sets the scale property. To use it, enter values in the
**X** and **Y** boxes and specify the unit.

**Tip** : You can enter `%` or `px` after values. This automatically changes
the displayed unit in the unit selector. You can also drag to define the
values in the **X** and **Y** boxes.

### Rotate

The **Rotate** control sets the rotate property. To use it, enter a value and
specify the unit.

**Tip** : You can type `deg`, `grad`, `rad`, or `turn` after a value in the
**Rotate** box. This automatically changes the displayed unit in the unit
selector.

## USS transform properties

You can use styling rules to set the transform properties for a visual
element. You can set the styling rules within a USS file or inline in a UXML
file.

### `transform-origin`

The `transform-origin` property sets the transform origin along the X and Y
axes in **pixels** The smallest unit in a computer image. Pixel size depends
on your screen resolution. Pixel lighting is calculated at every screen pixel.
[More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) or percentages.

You can also use keywords to set the value of the `transform-origin`
attribute. These keywords match the dots in the widget in the UI Builder. The
following keywords are supported:

**Pivot point** | **Keywords**  
---|---  
**Center** | 

  * `center`
  * `center center` (This is the default value)

  
**Center of left edge** | 

  * `left`
  * `left center`
  * `center left`

  
**Center of right edge** | 

  * `right`
  * `right center`
  * `center right`

  
**Center of top edge** | 

  * `top`
  * `top center`
  * `center top`

  
**Center of bottom edge** | 

  * `bottom`
  * `bottom center`
  * `center bottom`

  
**Top-left corner** | 

  * `top left`
  * `left top`

  
**Top-right corner** | 

  * `top right`
  * `right top`

  
**Bottom-left corner** | 

  * `bottom left`
  * `left bottom`

  
**Bottom-right corner** | 

  * `bottom right`
  * `right bottom`

  
  
**Examples**

    
    
    transform-origin: 0% 100%;
    transform-origin: 20px 10px;
    transform-origin: 0px 100%;
    transform-origin: 60% 10px;
    

### `translate`

The `translate` property sets the translation along the X and Y axes in pixels
or percentages relative to the size of this visual element. You can omit Y if
it equals X.

**Examples**

    
    
    translate: 80%;
    translate: 35px;
    translate: 5% 10px;
    translate: 24px 0%;
    

### `scale`

The `scale` property sets the scale along the X and Y axes in pixels or
percentages. You can omit Y if it equals X.

The keyword `none` sets no scale.

**Examples**

    
    
    scale: 2.5;
    scale: -1 1;
    scale: none;
    

### `rotate`

The `rotate` property sets the rotation using a number or a unit.

The keyword `none` sets no rotation.

**Examples**

    
    
    rotate: 45deg;
    rotate: -100grad;
    rotate: -3.14rad;
    rotate: 0.75turn;
    rotate: none;
    

##  Transform C# properties

You can set the transform properties for a visual element in a C# script.

### `IStyle.transformOrigin`

The [`IStyle.transformOrigin`](../ScriptReference/UIElements.IStyle-
transformOrigin.html) property sets the transform origin.

The `transformOrigin` property of the
[`style`](../ScriptReference/UIElements.VisualElement-style.html) is of type
[`StyleTransformOrigin`](../ScriptReference/UIElements.StyleTransformOrigin.html).
Its [constructor](../ScriptReference/UIElements.StyleTransformOrigin-
ctor.html) takes a
[`TransformOrigin`](../ScriptReference/UIElements.TransformOrigin.html) as an
argument. You can construct a new
[`TransformOrigin`](../ScriptReference/UIElements.TransformOrigin.html) using
an X value and a Y value. The X value and the Y value are of type
[`Length`](../ScriptReference/UIElements.Length.html).

**Examples**

    
    
    //This example sets the transform origin of the element to be 100 pixels from the left edge and 50% of the way down from the top edge.
    element.style.transformOrigin = new StyleTransformOrigin(new TransformOrigin(new Length(100f, LengthUnit.Pixel), new Length(50f, LengthUnit.Percent)));
    

You can simplify the above code as follows using implicit conversions:

    
    
    element.style.transformOrigin = new TransformOrigin(100, Length.Percent(50));
    

### `IStyle.translate`

The [`IStyle.translate`](../ScriptReference/UIElements.IStyle-translate.html)
property sets the translation.

[`IStyle.translate`](../ScriptReference/UIElements.IStyle-translate.html) is
of type [`StyleTranslate`](../ScriptReference/UIElements.StyleTranslate.html).
Its constructor takes a
[`Translate`](../ScriptReference/UIElements.Translate.html) as an argument.
You can construct a new
[`Translate`](../ScriptReference/UIElements.Translate.html) using an X value
and a Y value. The X value and the Y value are of type
[`Length`](../ScriptReference/UIElements.Length.html).

**Examples**

    
    
    //This example sets the translation of the element. The X-axis is 10% and the Y-axis is 50 pixels.
    element.style.translate = new StyleTranslate(new Translate(new Length(10f, LengthUnit.Percent), new Length(50f, LengthUnit.Pixel)));
    

You can simplify the above code as follows using implicit conversions:

    
    
    element.style.translate = new Translate(Length.Percent(10), 50);
    

### `IStyle.scale`

The [`IStyle.scale`](../ScriptReference/UIElements.IStyle-scale.html) property
sets the scale.

[`IStyle.scale`](../ScriptReference/UIElements.IStyle-scale.html) is of type
[`StyleScale`](../ScriptReference/UIElements.StyleScale.html).
[`StyleScale`](../ScriptReference/UIElements.StyleScale.html)’s
[constructor](../ScriptReference/UIElements.StyleScale-ctor.html) takes a
[Scale](../ScriptReference/UIElements.Scale.html) as an argument. You can
[construct](../ScriptReference/UIElements.Scale-ctor.html) this `Scale` with a
`Vector2`.

**Examples**

    
    
    element.style.scale = new StyleScale(new Scale(new Vector2(0.5f, -1f)));
    

You can simplify the code above as follows using implicit conversions:

    
    
    element.style.scale = new Scale(new Vector2(0.5f, -1));
    

### `IStyle.rotate`

The [`IStyle.rotate`](../ScriptReference/UIElements.IStyle-rotate.html)
property sets the rotation.

The [`IStyle.rotate`](../ScriptReference/UIElements.IStyle-rotate.html)
property is of type
[`StyleRotate`](../ScriptReference/UIElements.StyleRotate.html). The
[`StyleRotate`](../ScriptReference/UIElements.StyleRotate.html)’s
[constructor](../ScriptReference/UIElements.StyleRotate-ctor.html) takes a
[`Rotate`](../ScriptReference/UIElements.Rotate.html) as an argument. You can
[construct](../ScriptReference/UIElements.Rotate-ctor.html) this `Rotate` with
an [`Angle`](../ScriptReference/UIElements.Angle.html). You can
[construct](../ScriptReference/UIElements.Angle-ctor.html) an `Angle` with a
float and an optional
[`AngleUnit`](../ScriptReference/UIElements.AngleUnit.html) enum, or you can
use static methods
[`Degrees()`](../ScriptReference/UIElements.Angle.Degrees.html),
[`Gradians()`](../ScriptReference/UIElements.Angle.Gradians.html),
[`Radians()`](../ScriptReference/UIElements.Angle.Radians.html), and
[`Turns()`](../ScriptReference/UIElements.Angle.Turns.html).

**Examples**

    
    
    //Rotate by 180 degrees
    elements[0].style.rotate = new StyleRotate(new Rotate(new Angle(180f, AngleUnit.Degree)));
    //Rotate by 200 gradians
    elements[1].style.rotate = new StyleRotate(new Rotate(new Angle(200f, AngleUnit.Gradian)));
    //Rotate by pi radians
    elements[2].style.rotate = new StyleRotate(new Rotate(new Angle(Mathf.PI, AngleUnit.Radian)));
    //Rotate by half a turn
    elements[3].style.rotate = new StyleRotate(new Rotate(new Angle(0.5f, AngleUnit.Turn)));
    

You can simplify the above code as follows:

    
    
    //Rotate by 180 degrees
    elements[0].style.rotate = new Rotate(180);
    //Rotate by 200 gradians
    elements[1].style.rotate = new Rotate(Angle.Gradians(200));
    //Rotate by pi radians
    elements[2].style.rotate = new Rotate(Angle.Radians(Mathf.PI));
    //Rotate by half a turn
    elements[3].style.rotate = new Rotate(Angle.Turns(0.5f));
    

## Additional resources

  * [Layout engine](UIE-LayoutEngine.html)
  * [CSS transform-origin property](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) (Mozilla developer documentation)
  * [CSS translate property](https://developer.mozilla.org/en-US/docs/Web/CSS/translate) (Mozilla developer documentation)
  * [CSS rotate property](https://developer.mozilla.org/en-US/docs/Web/CSS/rotate) (Mozilla developer documentation)
  * [CSS scale property](https://developer.mozilla.org/en-US/docs/Web/CSS/scale) (Mozilla developer documentation)

[](UIE-image-import-settings.html)

Image import settings

[](UIE-Transitions.html)

USS transition

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

