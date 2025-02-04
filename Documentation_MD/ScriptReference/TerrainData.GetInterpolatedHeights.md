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

#  [TerrainData](TerrainData.html).GetInterpolatedHeights

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

## Declaration

public float[,] GetInterpolatedHeights(float xBase, float yBase, int xCount,
int yCount, float xInterval, float yInterval);

### Parameters

xBase | The base x coordinate.  
---|---  
yBase | The base y coordinate.  
xCount | The number of queries along the X axis.  
yCount | The number of queries along the Y axis.  
xInterval | The interval between each query along the X axis.  
yInterval | The interval between each query along the Y axis.  
  
### Description

Gets an array of terrain height values using the normalized x,y coordinates.

The function returns a two-dimensional array of size [yCount, xCount]. Each
returned value is an interpolation between the four neighboring Terrain height
samples, based on where the sampling point is located within the quad of the
four neighboring samples. The sampling points are evenly distributed, starting
at (xBase, yBase). Points are spaced `xInterval` apart along the X axis, and
`yInterval` apart along the Y axis. All the floating point arguments are
specified as normalized coordinates, with 0 indicating the left/top border of
the Terrain, and 1 indicating the right/bottom border of the Terrain. If a
sampling point is placed outside of [0,1], it is clamped to the range.

* * *

## Declaration

public void GetInterpolatedHeights(float[,] results, int resultXOffset, int
resultYOffset, float xBase, float yBase, int xCount, int yCount, float
xInterval, float yInterval);

### Parameters

results | The array to fill with height values.  
---|---  
resultXOffset | The offset from the beginning of the array, along the X axis, at which to start filling in height values.  
resultYOffset | The offset from the beginning of the array, along the Y axis, at which to start filling in height values.  
xBase | The base x coordinate.  
yBase | The base y coordinate.  
xCount | The number of queries along the X axis.  
yCount | The number of queries along the Y axis.  
xInterval | The interval between each query along the X axis.  
yInterval | The interval between each query along the Y axis.  
  
### Description

Fills the array with Terrain height values using normalized x,y coordinates.

The function takes a two-dimensional array, and fills height values into the
part starting at (resultXOffset, resultYOffset). Unlike the function overload
above, Unity guarantees not to allocate any memory during calls to the
`GetInterpolatedHeights` function.

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

