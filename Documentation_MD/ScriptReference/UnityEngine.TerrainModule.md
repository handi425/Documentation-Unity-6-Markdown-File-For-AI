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

# UnityEngine.TerrainModule

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

The Terrain module implements Unity's Terrain rendering engine available
through the Terrain component.

### Classes

[DetailPrototype](DetailPrototype.html)| Detail prototype used by the Terrain
GameObject.  
---|---  
[PaintContext](TerrainTools.PaintContext.html)| The context for a paint
operation that may span multiple connected Terrain tiles.  
[SpeedTreeWindAsset](SpeedTreeWindAsset.html)| SpeedTreeWindAsset generated by
the SpeedTreeImporter, contains wind version and configuration data for
SpeedTree wind simulation.  
[Terrain](Terrain.html)| The Terrain component renders the terrain.  
[TerrainCallbacks](TerrainCallbacks.html)| This static class provides events
that Unity triggers when Terrain data changes.  
[TerrainData](TerrainData.html)| The TerrainData class stores heightmaps,
detail mesh positions, tree instances, and terrain texture alpha maps.  
[TerrainExtensions](TerrainExtensions.html)| Extension methods to the Terrain
class, used only for the UpdateGIMaterials method used by the Global
Illumination System.  
[TerrainLayer](TerrainLayer.html)| Description of a terrain layer.  
[TerrainMap](TerrainUtils.TerrainMap.html)| Type for mapping 2D (X,Z) tile
coordinates to a Terrain object.  
[TerrainPaintUtility](TerrainTools.TerrainPaintUtility.html)| A set of utility
functions for custom terrain paint tools.  
[TerrainUtility](TerrainUtils.TerrainUtility.html)| Provides a set of utility
functions that are used by the terrain tools.  
[Tree](Tree.html)| Tree Component for the tree creator.  
[TreePrototype](TreePrototype.html)| Simple class that contains a pointer to a
tree prototype.  
  
### Structs

[BrushTransform](TerrainTools.BrushTransform.html)| Represents a linear 2D
transformation between brush UV space and a target XY space (typically this is
a Terrain-local object space.)  
---|---  
[DetailInstanceTransform](DetailInstanceTransform.html)| Describes the
transform of a Terrain detail object.  
[PatchExtents](PatchExtents.html)| Structure containing minimum and maximum
terrain patch height values.  
[TerrainTileCoord](TerrainUtils.TerrainTileCoord.html)| Specifies a set of 2D
tile coordinates.  
[TreeInstance](TreeInstance.html)| Contains information about a tree placed in
the Terrain game object.  
  
### Enumerations

[DetailRenderMode](DetailRenderMode.html)| Render mode for detail prototypes.  
---|---  
[DetailScatterMode](DetailScatterMode.html)| Provides options to specify how
details are scattered on the terrain.  
[TerrainBuiltinPaintMaterialPasses](TerrainTools.TerrainBuiltinPaintMaterialPasses.html)|
Built-in render passes for paint material.  
[TerrainChangedFlags](TerrainChangedFlags.html)| Indicate the types of changes
to the terrain in OnTerrainChanged callback.  
[TerrainHeightmapSyncControl](TerrainHeightmapSyncControl.html)| Controls what
Terrain heightmap data to synchronize when there are changes to the heightmap
texture.  
[TerrainLayerSmoothnessSource](TerrainLayerSmoothnessSource.html)| Source of
smoothness value used in the underlying splat material of a TerrainLayer when
TerrainLayer.diffuseTexture has an alpha channel.  
[TerrainRenderFlags](TerrainRenderFlags.html)| Enum provding terrain rendering
options.  
[TreeMotionVectorModeOverride](TreeMotionVectorModeOverride.html)| Options for
motion vector rendering on the terrain.  
  
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

