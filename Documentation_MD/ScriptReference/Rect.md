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

# Rect

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

A 2D Rectangle defined by X and Y position, width and height.

Unity uses a number of 2D coordinate spaces, most of which define X as
increasing to the right, and Y increasing upwards. The one exception is in the
GUI and GUILayout classes, where Y increases downwards.  
  
The following examples are illustrated in GUI space, where (0,0) represents
the top-left corner and Y increases downwards.  
  
Rectangles can be specified in two different ways. The first is with an
[x](Rect-x.html) and [y](Rect-y.html) position and a [width](Rect-width.html)
and [height](Rect-height.html):  
  
![](../StaticFiles/ScriptRefImages/RectXY.svg)  
  
The other way is with the X and Y coordinates of each of its edges. These are
called [xMin](Rect-xMin.html), [xMax](Rect-xMax.html), [yMin](Rect-yMin.html)
and [yMax](Rect-yMax.html):  
  
![](../StaticFiles/ScriptRefImages/RectXMinYMin.svg)  
  
Note that although `x` and `y` have the same values as `xMin` and `yMin`, they
behave differently when you set them. Setting `x` or `y` changes the position
of the rectangle, but preserves its size:  
  
![](../StaticFiles/ScriptRefImages/RectSetX.svg)  
  
Setting any of `xMin`, `xMax`, `yMin` and `yMax` will resize the rectangle,
but preserve the position of the opposite edge:  
  
![](../StaticFiles/ScriptRefImages/RectSetXMin.svg)  
  
Additional resources: [GUI Scripting Guide](../Manual/gui-Basics.html),
[Camera.rect](Camera-rect.html), [Camera.pixelRect](Camera-pixelRect.html).

### Static Properties

[zero](Rect-zero.html)| Shorthand for writing new Rect(0,0,0,0).  
---|---  
  
### Properties

[center](Rect-center.html)| The position of the center of the rectangle.  
---|---  
[height](Rect-height.html)| The height of the rectangle, measured from the Y
position.  
[max](Rect-max.html)| The position of the maximum corner of the rectangle.  
[min](Rect-min.html)| The position of the minimum corner of the rectangle.  
[position](Rect-position.html)| The X and Y position of the rectangle.  
[size](Rect-size.html)| The width and height of the rectangle.  
[width](Rect-width.html)| The width of the rectangle, measured from the X
position.  
[x](Rect-x.html)| The X coordinate of the rectangle.  
[xMax](Rect-xMax.html)| The maximum X coordinate of the rectangle.  
[xMin](Rect-xMin.html)| The minimum X coordinate of the rectangle.  
[y](Rect-y.html)| The Y coordinate of the rectangle.  
[yMax](Rect-yMax.html)| The maximum Y coordinate of the rectangle.  
[yMin](Rect-yMin.html)| The minimum Y coordinate of the rectangle.  
  
### Constructors

[Rect](Rect-ctor.html)| Creates a new rectangle.  
---|---  
  
### Public Methods

[Contains](Rect.Contains.html)| Returns true if the x and y components of
point is a point inside this rectangle. If allowInverse is present and true,
the width and height of the Rect are allowed to take negative values (ie, the
min value is greater than the max), and the test will still work.  
---|---  
[Overlaps](Rect.Overlaps.html)| Returns true if the other rectangle overlaps
this one. If allowInverse is present and true, the widths and heights of the
Rects are allowed to take negative values (ie, the min value is greater than
the max), and the test will still work.  
[Set](Rect.Set.html)| Set components of an existing Rect.  
[ToString](Rect.ToString.html)| Returns a formatted string for this Rect.  
  
### Static Methods

[MinMaxRect](Rect.MinMaxRect.html)| Creates a rectangle from min/max
coordinate values.  
---|---  
[NormalizedToPoint](Rect.NormalizedToPoint.html)| Returns a point inside a
rectangle, given normalized coordinates.  
[PointToNormalized](Rect.PointToNormalized.html)| Returns the normalized
coordinates cooresponding the the point.  
  
### Operators

[operator ==](Rect-operator_eq.html)| Returns true if the rectangles are the
same.  
---|---  
  
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

