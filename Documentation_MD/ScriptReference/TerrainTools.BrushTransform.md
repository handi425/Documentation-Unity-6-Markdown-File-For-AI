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

# BrushTransform

struct in UnityEngine.TerrainTools

/

Implemented in:[UnityEngine.TerrainModule](UnityEngine.TerrainModule.html)

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

Represents a linear 2D transformation between brush UV space and a target XY
space (typically this is a Terrain-local object space.)

The BrushTransform represents a rectangular brush, with scale, rotation, and
skew. The brush is assumed to lie in the [0,1] range in brush UV space.  
  
The transform and its inverse are represented as follows:  
`xy = u * BrushTransform.brushU + v * BrushTransform.brushV +
BrushTransform.brushOrigin`  
`uv = x * BrushTransform.targetX + y * BrushTransform.targetY +
BrushTransform.targetOrigin`  

### Properties

[brushOrigin](TerrainTools.BrushTransform-brushOrigin.html)| (Read Only) Brush
UV origin, in XY space.  
---|---  
[brushU](TerrainTools.BrushTransform-brushU.html)| (Read Only) Brush U vector,
in XY space.  
[brushV](TerrainTools.BrushTransform-brushV.html)| (Read Only) Brush V vector,
in XY space.  
[targetOrigin](TerrainTools.BrushTransform-targetOrigin.html)| (Read Only)
Target XY origin, in Brush UV space.  
[targetX](TerrainTools.BrushTransform-targetX.html)| (Read Only) Target X
vector, in Brush UV space.  
[targetY](TerrainTools.BrushTransform-targetY.html)| (Read Only) Target Y
vector, in Brush UV space.  
  
### Constructors

[BrushTransform](TerrainTools.BrushTransform-ctor.html)| Creates a
BrushTransform.  
---|---  
  
### Public Methods

[FromBrushUV](TerrainTools.BrushTransform.FromBrushUV.html)| Applies the
transform to convert a Brush UV coordinate to the target XY space.  
---|---  
[GetBrushXYBounds](TerrainTools.BrushTransform.GetBrushXYBounds.html)| Get the
axis-aligned bounding rectangle of the brush, in target XY space.  
[ToBrushUV](TerrainTools.BrushTransform.ToBrushUV.html)| Applies the transform
to convert a target XY coordinate to Brush UV space.  
  
### Static Methods

[FromRect](TerrainTools.BrushTransform.FromRect.html)| Creates an axis-aligned
BrushTransform from a rectangle.  
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

