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

# TerrainPaintUtility

class in UnityEngine.TerrainTools

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

A set of utility functions for custom terrain paint tools.

### Static Methods

[BeginPaintHeightmap](TerrainTools.TerrainPaintUtility.BeginPaintHeightmap.html)|
Helper function to set up a PaintContext for modifying the heightmap of one or
more Terrain tiles.  
---|---  
[BeginPaintHoles](TerrainTools.TerrainPaintUtility.BeginPaintHoles.html)|
Helper function to set up a PaintContext for modifying the Terrain holes of
one or more Terrain tiles.  
[BeginPaintTexture](TerrainTools.TerrainPaintUtility.BeginPaintTexture.html)|
Helper function to set up a PaintContext for modifying the alphamap of one or
more Terrain tiles.  
[BuildTransformPaintContextUVToPaintContextUV](TerrainTools.TerrainPaintUtility.BuildTransformPaintContextUVToPaintContextUV.html)|
Builds a Scale & Offset transform to convert between one PaintContext's UV
space and another PaintContext's UV space.  
[CalculateBrushTransform](TerrainTools.TerrainPaintUtility.CalculateBrushTransform.html)|
Creates a BrushTransform from the input parameters.  
[CollectNormals](TerrainTools.TerrainPaintUtility.CollectNormals.html)| Helper
function to set up a PaintContext that collects mesh normal data from one or
more Terrain tiles.  
[EndPaintHeightmap](TerrainTools.TerrainPaintUtility.EndPaintHeightmap.html)|
Helper function to complete a heightmap modification.  
[EndPaintHoles](TerrainTools.TerrainPaintUtility.EndPaintHoles.html)| Helper
function to complete a Terrain holes modification.  
[EndPaintTexture](TerrainTools.TerrainPaintUtility.EndPaintTexture.html)|
Helper function to complete a texture alphamap modification.  
[FindTerrainLayerIndex](TerrainTools.TerrainPaintUtility.FindTerrainLayerIndex.html)|
Finds the index of a TerrainLayer in a Terrain tile.  
[GetBlitMaterial](TerrainTools.TerrainPaintUtility.GetBlitMaterial.html)|
Returns the default material for blitting operations.  
[GetBrushWorldSizeLimits](TerrainTools.TerrainPaintUtility.GetBrushWorldSizeLimits.html)|
Calculates the minimum and maximum Brush size limits, in world space.  
[GetBuiltinPaintMaterial](TerrainTools.TerrainPaintUtility.GetBuiltinPaintMaterial.html)|
Returns the built-in in paint material used by the built-in tools.  
[GetCopyTerrainLayerMaterial](TerrainTools.TerrainPaintUtility.GetCopyTerrainLayerMaterial.html)|
Returns the default copy terrain layer material.  
[GetHeightBlitMaterial](TerrainTools.TerrainPaintUtility.GetHeightBlitMaterial.html)|
Returns the Material to use when copying the Terrain heightmap.  
[GetTerrainAlphaMapChecked](TerrainTools.TerrainPaintUtility.GetTerrainAlphaMapChecked.html)|
Returns the alphamap texture at mapIndex.  
[ReleaseContextResources](TerrainTools.TerrainPaintUtility.ReleaseContextResources.html)|
Releases the allocated resources of the specified PaintContext.  
[SetupTerrainToolMaterialProperties](TerrainTools.TerrainPaintUtility.SetupTerrainToolMaterialProperties.html)|
Sets up all of the material properties used by functions in TerrainTool.cginc.  
  
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

