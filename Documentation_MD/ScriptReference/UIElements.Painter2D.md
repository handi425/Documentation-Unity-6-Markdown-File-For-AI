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

# Painter2D

class in UnityEngine.UIElements

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

Object to draw 2D vector graphics.

The example below demonstrates how to use the Painter2D class to draw content
in a [VisualElement](UIElements.VisualElement.html) with the
[VisualElement.generateVisualContent](UIElements.VisualElement-
generateVisualContent.html) callback. You can also create a standalone
[Painter2D.Painter2D](UIElements.Painter2D-ctor.html) object to draw content
offscreen, and use the
[Painter2D.SaveToVectorImage](UIElements.Painter2D.SaveToVectorImage.html)
method to save the painter content in a
[VectorImage](UIElements.VectorImage.html) asset.  
  

    
    
     using UnityEngine;
     using UnityEngine.UIElements;  
      
     [[RequireComponent](RequireComponent.html)(typeof([UIDocument](UIElements.UIDocument.html)))]
     public class Painter2DExample : [MonoBehaviour](MonoBehaviour.html)
     {
         public void OnEnable()
         {
             var doc = GetComponent<[UIDocument](UIElements.UIDocument.html)>();
             doc.rootVisualElement.generateVisualContent += Draw;
         }  
      
         void Draw([MeshGenerationContext](UIElements.MeshGenerationContext.html) ctx)
         {
             var painter = ctx.painter2D;
             painter.lineWidth = 10.0f;
             painter.lineCap = [LineCap.Round](UIElements.LineCap.Round.html);
             painter.strokeGradient = new [Gradient](Gradient.html)() {
                 colorKeys = new [GradientColorKey](GradientColorKey.html)[] {
                     new [GradientColorKey](GradientColorKey.html)() { color = [Color.red](Color-red.html), time = 0.0f },
                     new [GradientColorKey](GradientColorKey.html)() { color = [Color.blue](Color-blue.html), time = 1.0f }
                 }
             };
             painter.BeginPath();
             painter.MoveTo(new [Vector2](Vector2.html)(10, 10));
             painter.BezierCurveTo(new [Vector2](Vector2.html)(100, 100), new [Vector2](Vector2.html)(200, 0), new [Vector2](Vector2.html)(300, 100));
             painter.Stroke();
         }
     }
    

### Properties

[fillColor](UIElements.Painter2D-fillColor.html)|  The color used for fill
paths when using Fill.  
---|---  
[lineCap](UIElements.Painter2D-lineCap.html)|  The cap to use when drawing
paths using Stroke.  
[lineJoin](UIElements.Painter2D-lineJoin.html)|  The join to use when drawing
paths using Stroke.  
[lineWidth](UIElements.Painter2D-lineWidth.html)|  The line width of draw
paths when using Stroke.  
[miterLimit](UIElements.Painter2D-miterLimit.html)|  When using LineJoin.Miter
joins, this defines the limit on the ratio of the miter length to the stroke
width before converting the miter to a bevel.  
[strokeColor](UIElements.Painter2D-strokeColor.html)|  The color of draw paths
when using Stroke.  
[strokeGradient](UIElements.Painter2D-strokeGradient.html)|  The stroke
gradient to use when using Stroke.  
  
### Constructors

[Painter2D](UIElements.Painter2D-ctor.html)|  Initializes an instance of
Painter2D.  
---|---  
  
### Public Methods

[Arc](UIElements.Painter2D.Arc.html)|  Adds an arc to the current sub-path to
the provided position, radius and angles.  
---|---  
[ArcTo](UIElements.Painter2D.ArcTo.html)|  Adds an arc to the current sub-path
to the provided position using a control point.  
[BeginPath](UIElements.Painter2D.BeginPath.html)|  Begins a new path and
empties the list of recorded sub-paths.  
[BezierCurveTo](UIElements.Painter2D.BezierCurveTo.html)|  Adds a cubic bezier
curve to the current sub-path to the provided position using two control
points.  
[Clear](UIElements.Painter2D.Clear.html)|  When created as a detached painter,
clears the current content. Does nothing otherwise.  
[ClosePath](UIElements.Painter2D.ClosePath.html)|  Closes the current sub-path
with a straight line. If the sub-path is already closed, this does nothing.  
[Dispose](UIElements.Painter2D.Dispose.html)|  Dispose the Painter2D object
and free its internal unmanaged resources.  
[Fill](UIElements.Painter2D.Fill.html)|  Fills the currently defined path.  
[LineTo](UIElements.Painter2D.LineTo.html)|  Adds a straight line to the
current sub-path to the provided position.  
[MoveTo](UIElements.Painter2D.MoveTo.html)|  Begins a new sub-path at the
provied coordinate.  
[QuadraticCurveTo](UIElements.Painter2D.QuadraticCurveTo.html)|  Adds a
quadratic bezier curve to the current sub-path to the provided position using
a control point.  
[SaveToVectorImage](UIElements.Painter2D.SaveToVectorImage.html)|  Saves the
content of this Painter2D to a VectorImage object.  
[Stroke](UIElements.Painter2D.Stroke.html)|  Strokes the currently defined
path.  
  
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

