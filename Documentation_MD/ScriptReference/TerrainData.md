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

# TerrainData

class in UnityEngine

/

Inherits from:[Object](Object.html)

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

The TerrainData class stores heightmaps, detail mesh positions, tree
instances, and terrain texture alpha maps.

The [Terrain](Terrain.html) component links to the terrain data and renders
it.

### Static Properties

[AlphamapTextureName](TerrainData.AlphamapTextureName.html)| The name for the
Terrain alpha map textures.  
---|---  
[HolesTextureName](TerrainData.HolesTextureName.html)| The name for the
Terrain holes Texture.  
  
### Properties

[alphamapHeight](TerrainData-alphamapHeight.html)| Height of the alpha map.
(Read only.)  
---|---  
[alphamapLayers](TerrainData-alphamapLayers.html)| Number of alpha map layers.  
[alphamapResolution](TerrainData-alphamapResolution.html)| The size of the
alpha map in texels for either the width or the height.  
[alphamapTextureCount](TerrainData-alphamapTextureCount.html)| Returns the
number of alphamap textures.  
[alphamapTextures](TerrainData-alphamapTextures.html)| Alpha map textures used
by the Terrain. Used by Terrain Inspector for undo.  
[alphamapWidth](TerrainData-alphamapWidth.html)| Width of the alpha map.  
[baseMapResolution](TerrainData-baseMapResolution.html)| Resolution of the
base map used for rendering far patches on the terrain.  
[bounds](TerrainData-bounds.html)| The local bounding box of the TerrainData
object.  
[detailHeight](TerrainData-detailHeight.html)| The resolution of the detail
data stored in TerrainData.  
[detailPatchCount](TerrainData-detailPatchCount.html)| The number of patches
along a terrain tile edge. This is squared to make a grid of patches.  
[detailPrototypes](TerrainData-detailPrototypes.html)| Contains the detail
texture/meshes that the Terrain has.  
[detailResolution](TerrainData-detailResolution.html)| Detail Resolution of
the TerrainData.  
[detailResolutionPerPatch](TerrainData-detailResolutionPerPatch.html)| Detail
Resolution of each patch. A larger value will decrease the number of batches
used by detail objects.  
[detailScatterMode](TerrainData-detailScatterMode.html)| Additional resources:
DetailScatterMode  
[detailWidth](TerrainData-detailWidth.html)| The resolution of the detail data
stored in TerrainData.  
[enableHolesTextureCompression](TerrainData-
enableHolesTextureCompression.html)| Enable the Terrain holes Texture
compression.  
[heightmapResolution](TerrainData-heightmapResolution.html)| The size of the
heightmap in texels for either the width or the height.  
[heightmapScale](TerrainData-heightmapScale.html)| Returns a Vector3 where the
x and z components are the size of each heightmap sample (i.e. the space
between two neighboring heightmap samples), and the y component is the entire
Terrain's height range in world space.  
[heightmapTexture](TerrainData-heightmapTexture.html)| Returns the heightmap
texture.  
[holesResolution](TerrainData-holesResolution.html)| Returns the Terrain holes
resolution for both the data and the Texture.  
[holesTexture](TerrainData-holesTexture.html)| Returns the Terrain holes
Texture.  
[maxDetailScatterPerRes](TerrainData-maxDetailScatterPerRes.html)| The maximum
value of each sample in the detail map of the terrain data.  
[size](TerrainData-size.html)| The total size in world units of the terrain.  
[terrainLayers](TerrainData-terrainLayers.html)| Retrieves the terrain layers
used by the current terrain.  
[treeInstanceCount](TerrainData-treeInstanceCount.html)| Returns the number of
tree instances.  
[treeInstances](TerrainData-treeInstances.html)| Contains the current trees
placed in the terrain.  
[treePrototypes](TerrainData-treePrototypes.html)| The list of tree prototypes
available in the inspector.  
[wavingGrassAmount](TerrainData-wavingGrassAmount.html)| Amount of waving
grass in the terrain.  
[wavingGrassSpeed](TerrainData-wavingGrassSpeed.html)| Speed of the waving
grass.  
[wavingGrassStrength](TerrainData-wavingGrassStrength.html)| Strength of the
waving grass in the terrain.  
[wavingGrassTint](TerrainData-wavingGrassTint.html)| Color of the waving grass
that the terrain has.  
  
### Public Methods

[ComputeDetailCoverage](TerrainData.ComputeDetailCoverage.html)| This function
computes and returns the coverage (how many instances fit in a square unit) of
a detail prototype, given its index.  
---|---  
[ComputeDetailInstanceTransforms](TerrainData.ComputeDetailInstanceTransforms.html)|
This function computes and returns an array of detail object transforms for
the specified patch and the specified prototype. You can use this function to
retrieve the exact same transform data the Unity engine uses for detail
rendering.  
[CopyActiveRenderTextureToHeightmap](TerrainData.CopyActiveRenderTextureToHeightmap.html)|
Copies the specified part of the active RenderTexture to the Terrain heightmap
texture.  
[CopyActiveRenderTextureToTexture](TerrainData.CopyActiveRenderTextureToTexture.html)|
Copies the specified part of the active RenderTexture to the Terrain texture.  
[DirtyHeightmapRegion](TerrainData.DirtyHeightmapRegion.html)| Marks the
specified part of the heightmap as dirty.  
[DirtyTextureRegion](TerrainData.DirtyTextureRegion.html)| Marks the specified
part of the Terrain texture as dirty.  
[GetAlphamaps](TerrainData.GetAlphamaps.html)| Returns the alpha map at a
position x, y given a width and height.  
[GetAlphamapTexture](TerrainData.GetAlphamapTexture.html)| Returns the
alphamap texture at the specified index.  
[GetClampedDetailPatches](TerrainData.GetClampedDetailPatches.html)| Returns
an array of detail patches, which are each identified by X-Z coordinates.
Detail objects in the patches are clamped to the maximum count.  
[GetDetailLayer](TerrainData.GetDetailLayer.html)| Returns a 2D array of the
detail object density (i.e. the number of detail objects for this layer) in
the specific location.  
[GetHeight](TerrainData.GetHeight.html)| Gets the world space height of the
Terrain at a certain point x,y without adding the Terrain's world position y.  
[GetHeights](TerrainData.GetHeights.html)| Gets an array of heightmap samples.  
[GetHoles](TerrainData.GetHoles.html)| Gets an array of Terrain holes samples.  
[GetInterpolatedHeight](TerrainData.GetInterpolatedHeight.html)| Gets an
interpolated height at a point x,y. The x and y coordinates are clamped to [0,
1].  
[GetInterpolatedHeights](TerrainData.GetInterpolatedHeights.html)| Gets an
array of terrain height values using the normalized x,y coordinates.  
[GetInterpolatedNormal](TerrainData.GetInterpolatedNormal.html)| Get an
interpolated normal at a given location.  
[GetMaximumHeightError](TerrainData.GetMaximumHeightError.html)| Returns an
array of tesselation maximum height error values per renderable terrain patch.
The returned array can be modified and passed to OverrideMaximumHeightError.  
[GetPatchMinMaxHeights](TerrainData.GetPatchMinMaxHeights.html)| Returns an
array of min max height values for all the renderable patches in a terrain.
The returned array can be modified and then passed to
OverrideMinMaxPatchHeights.  
[GetSteepness](TerrainData.GetSteepness.html)| Gets the gradient of the
terrain at point (x,y). The gradient's value is always positive.  
[GetSupportedLayers](TerrainData.GetSupportedLayers.html)| Returns an array of
all supported detail layer indices in the area.  
[GetTreeInstance](TerrainData.GetTreeInstance.html)| Gets the tree instance at
the specified index. It is used as a faster version of treeInstances[index] as
this function doesn't create the entire tree instances array.  
[IsHole](TerrainData.IsHole.html)| Gets whether a certain point at x,y is a
hole.  
[OverrideMaximumHeightError](TerrainData.OverrideMaximumHeightError.html)|
Override the maximum tessellation height error with user provided values. Note
that the overriden values get reset when the terrain resolution is changed and
stays unchanged when the terrain heightmap is painted or changed via script.  
[OverrideMinMaxPatchHeights](TerrainData.OverrideMinMaxPatchHeights.html)|
Override the minimum and maximum patch heights for every renderable terrain
patch. Note that the overriden values get reset when the terrain resolution is
changed and stays unchanged when the terrain heightmap is painted or changed
via script.  
[RefreshPrototypes](TerrainData.RefreshPrototypes.html)| Reloads all the
values of the available prototypes (ie, detail mesh assets) in the TerrainData
Object.  
[RemoveDetailPrototype](TerrainData.RemoveDetailPrototype.html)| Removes the
detail prototype at the specified index.  
[SetAlphamaps](TerrainData.SetAlphamaps.html)| Assign all splat values in the
given map area.  
[SetBaseMapDirty](TerrainData.SetBaseMapDirty.html)| Marks the terrain data as
dirty to trigger an update of the terrain basemap texture.  
[SetDetailLayer](TerrainData.SetDetailLayer.html)| Sets the detail layer
density map.  
[SetDetailResolution](TerrainData.SetDetailResolution.html)| Sets the
resolution of the detail map.  
[SetDetailScatterMode](TerrainData.SetDetailScatterMode.html)| Sets the
DetailScatterMode.  
[SetHeights](TerrainData.SetHeights.html)| Sets an array of heightmap samples.  
[SetHeightsDelayLOD](TerrainData.SetHeightsDelayLOD.html)| Sets an array of
heightmap samples.  
[SetHoles](TerrainData.SetHoles.html)| Sets an array of Terrain holes samples.  
[SetHolesDelayLOD](TerrainData.SetHolesDelayLOD.html)| Sets an array of
Terrain holes samples.  
[SetTerrainLayersRegisterUndo](TerrainData.SetTerrainLayersRegisterUndo.html)|
This function sets the terrainLayers property, and in addition, registers the
action to the Editor's undo stack.  
[SetTreeInstance](TerrainData.SetTreeInstance.html)| Sets the tree instance
with new parameters at the specified index. However, you cannot change
TreeInstance.prototypeIndex and TreeInstance.position. If you change them, the
method throws an ArgumentException.  
[SetTreeInstances](TerrainData.SetTreeInstances.html)| Sets the Tree Instance
array, and optionally snaps Trees onto the surface of the Terrain heightmap.  
[SyncHeightmap](TerrainData.SyncHeightmap.html)| Performs synchronization
queued by previous calls to CopyActiveRenderTextureToHeightmap and
DirtyHeightmapRegion, which makes the height data and LOD data used for
tessellation up to date.  
[SyncTexture](TerrainData.SyncTexture.html)| Performs synchronization queued
by previous calls to CopyActiveRenderTextureToTexture and DirtyTextureRegion,
which makes CPU data of the Terrain textures up to date.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

