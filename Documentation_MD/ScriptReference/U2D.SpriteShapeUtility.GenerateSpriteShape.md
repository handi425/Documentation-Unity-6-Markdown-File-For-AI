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

#  [SpriteShapeUtility](U2D.SpriteShapeUtility.html).GenerateSpriteShape

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

public static void
GenerateSpriteShape([U2D.SpriteShapeRenderer](U2D.SpriteShapeRenderer.html)
renderer, [U2D.SpriteShapeParameters](U2D.SpriteShapeParameters.html)
shapeParams, ShapeControlPoint[] points, SpriteShapeMetaData[] metaData,
AngleRangeInfo[] angleRange, Sprite[] sprites, Sprite[] corners);

### Parameters

renderer | SpriteShapeRenderer to which the generated geometry is fed to.  
---|---  
shapeParams | Input parameters for the SpriteShape tessellator.  
points | A list of control points that describes the shape.  
metaData | Additional data about the shape's control point. This is useful during tessellation of the shape.  
sprites | The list of Sprites that could be used for the edges.  
corners | The list of Sprites that could be used for the corners.  
angleRange | A parameter that determins how to tessellate each of the edge.  
  
### Description

Generate a mesh based on input parameters.

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

