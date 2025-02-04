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

# IOnPaint

interface in UnityEditor.TerrainTools

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

Interface that provides parameters and utility functions for the OnPaint event
of the terrain paint tools.

Additional resources:
[TerrainPaintTool<T0>.OnPaint](TerrainTools.TerrainPaintTool_1.OnPaint.html).

### Properties

[brushSize](TerrainTools.IOnPaint-brushSize.html)| Read only. Current brush
size in Terrain units (equivalent size to world units).  
---|---  
[brushStrength](TerrainTools.IOnPaint-brushStrength.html)| Read only. Current
brush strength.  
[brushTexture](TerrainTools.IOnPaint-brushTexture.html)| Read only. Current
selected brush texture.  
[hitValidTerrain](TerrainTools.IOnPaint-hitValidTerrain.html)| Read only. True
if the mouse is over a valid Terrain object; otherwise false.  
[raycastHit](TerrainTools.IOnPaint-raycastHit.html)| Read only. The raycast
result for the current mouse position. This is valid when hitValidTerrain is
true.  
[uv](TerrainTools.IOnPaint-uv.html)| Read only. The normalized position
(between 0 and 1) on the active Terrain.  
  
### Public Methods

[Repaint](TerrainTools.IOnPaint.Repaint.html)| Instructs the Editor to repaint
the tool UI, the Scene view, or both.  
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

