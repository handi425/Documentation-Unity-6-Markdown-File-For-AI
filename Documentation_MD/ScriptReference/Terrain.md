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

# Terrain

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

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

The Terrain component renders the terrain.

### Static Properties

[activeTerrain](Terrain-activeTerrain.html)| The active Terrain. This is a
convenient function to get to the main Terrain in the Scene.  
---|---  
[activeTerrains](Terrain-activeTerrains.html)| The active terrains in the
Scene.  
[compressedHolesFormat](Terrain-compressedHolesFormat.html)| Graphics format
of the Terrain holes Texture when it is compressed.  
[compressedHolesTextureFormat](Terrain-compressedHolesTextureFormat.html)|
Texture format of the Terrain holes Texture when it is compressed.  
[heightmapFormat](Terrain-heightmapFormat.html)| Graphics format of the
Terrain heightmap.  
[heightmapRenderTextureFormat](Terrain-heightmapRenderTextureFormat.html)|
RenderTextureFormat of the terrain heightmap.  
[holesFormat](Terrain-holesFormat.html)| Graphics format of the Terrain holes
Texture when it is not compressed.  
[holesRenderTextureFormat](Terrain-holesRenderTextureFormat.html)| Render
texture format of the Terrain holes Texture.  
[normalmapFormat](Terrain-normalmapFormat.html)| Graphics format of the
Terrain normal map texture.  
[normalmapRenderTextureFormat](Terrain-normalmapRenderTextureFormat.html)|
Render texture format of the Terrain normal map texture.  
[normalmapTextureFormat](Terrain-normalmapTextureFormat.html)| Texture format
of the Terrain normal map texture.  
  
### Properties

[allowAutoConnect](Terrain-allowAutoConnect.html)| Specifies if the terrain
tile will be automatically connected to adjacent tiles.  
---|---  
[bakeLightProbesForTrees](Terrain-bakeLightProbesForTrees.html)| Whether to
bake an array of internal light probes for Tree Editor trees (Editor only).  
[basemapDistance](Terrain-basemapDistance.html)| Heightmap patches beyond
basemap distance will use a precomputed low res basemap.  
[bottomNeighbor](Terrain-bottomNeighbor.html)| Terrain bottom neighbor.  
[collectDetailPatches](Terrain-collectDetailPatches.html)| Collect detail
patches from memory.  
[deringLightProbesForTrees](Terrain-deringLightProbesForTrees.html)| Removes
ringing from light probes on Tree Editor trees (Editor only).  
[detailObjectDensity](Terrain-detailObjectDensity.html)| Density of detail
objects.  
[detailObjectDistance](Terrain-detailObjectDistance.html)| Detail objects will
be displayed up to this distance.  
[drawHeightmap](Terrain-drawHeightmap.html)| Indicates whether Unity draws the
Terrain geometry itself.  
[drawInstanced](Terrain-drawInstanced.html)| Set to true to enable the terrain
instance renderer. The default value is false.  
[drawTreesAndFoliage](Terrain-drawTreesAndFoliage.html)| Specify if terrain
trees and details should be drawn.  
[editorRenderFlags](Terrain-editorRenderFlags.html)| Controls what part of the
terrain should be rendered.  
[enableHeightmapRayTracing](Terrain-enableHeightmapRayTracing.html)| When this
options is enabled, Terrain heightmap geometries will be added in acceleration
structures used for Ray Tracing.  
[groupingID](Terrain-groupingID.html)| Grouping ID for auto connect.  
[heightmapMaximumLOD](Terrain-heightmapMaximumLOD.html)| Limits the Terrain's
maximum rendering resolution.  
[heightmapMinimumLODSimplification](Terrain-
heightmapMinimumLODSimplification.html)| Limits how simplified the rendered
terrain can be.  
[heightmapPixelError](Terrain-heightmapPixelError.html)| An approximation of
how many pixels the terrain will pop in the worst case when switching lod.  
[ignoreQualitySettings](Terrain-ignoreQualitySettings.html)| When enabled, the
terrain ignores the terrain overrides set in the QualitySettings.  
[keepUnusedRenderingResources](Terrain-keepUnusedRenderingResources.html)|
Defines whether Unity frees per-Camera rendering resources for the Terrain
when those resources aren't in use after a certain number of frames.  
[leftNeighbor](Terrain-leftNeighbor.html)| The Terrain tile to the left, which
is in the negative X direction.  
[lightmapIndex](Terrain-lightmapIndex.html)| The index of the baked lightmap
applied to this terrain.  
[lightmapScaleOffset](Terrain-lightmapScaleOffset.html)| The UV scale & offset
used for a baked lightmap.  
[materialTemplate](Terrain-materialTemplate.html)| The custom material Unity
uses to render the Terrain.  
[normalmapTexture](Terrain-normalmapTexture.html)| Returns the normal map
texture computed from sampling the heightmap. It is only used when terrain is
rendered using instancing.  
[patchBoundsMultiplier](Terrain-patchBoundsMultiplier.html)| Set the terrain
bounding box scale.  
[preserveTreePrototypeLayers](Terrain-preserveTreePrototypeLayers.html)|
Allows you to specify how Unity chooses the layer for tree instances.  
[realtimeLightmapIndex](Terrain-realtimeLightmapIndex.html)| The index of the
realtime lightmap applied to this terrain.  
[realtimeLightmapScaleOffset](Terrain-realtimeLightmapScaleOffset.html)| The
UV scale & offset used for a realtime lightmap.  
[reflectionProbeUsage](Terrain-reflectionProbeUsage.html)| How reflection
probes are used for terrain. See ReflectionProbeUsage.  
[renderingLayerMask](Terrain-renderingLayerMask.html)| Determines which
rendering layers the Terrain renderer lives on.  
[rightNeighbor](Terrain-rightNeighbor.html)| The Terrain tile to the left,
which is in the positive X direction.  
[shadowCastingMode](Terrain-shadowCastingMode.html)| Allows you to set the
shadow casting mode for the terrain.  
[terrainData](Terrain-terrainData.html)| The Terrain Data that stores
heightmaps, terrain textures, detail meshes and trees.  
[topNeighbor](Terrain-topNeighbor.html)| Terrain top neighbor.  
[treeBillboardDistance](Terrain-treeBillboardDistance.html)| Distance from the
camera where trees will be rendered as billboards only.  
[treeCrossFadeLength](Terrain-treeCrossFadeLength.html)| Total distance delta
that trees will use to transition from billboard orientation to mesh
orientation.  
[treeDistance](Terrain-treeDistance.html)| The maximum distance at which trees
are rendered.  
[treeLODBiasMultiplier](Terrain-treeLODBiasMultiplier.html)| The multiplier to
the current LOD bias used for rendering LOD trees (i.e. SpeedTree trees).  
[treeMaximumFullLODCount](Terrain-treeMaximumFullLODCount.html)| Maximum
number of trees rendered at full LOD.  
[treeMotionVectorModeOverride](Terrain-treeMotionVectorModeOverride.html)| The
motion vector rendering mode for all SpeedTree models painted on the terrain.  
  
### Public Methods

[AddTreeInstance](Terrain.AddTreeInstance.html)| Adds a tree instance to the
terrain.  
---|---  
[Flush](Terrain.Flush.html)| Flushes any change done in the terrain so it
takes effect.  
[GetClosestReflectionProbes](Terrain.GetClosestReflectionProbes.html)| Fills
the list with reflection probes whose AABB intersects with terrain's AABB.
Their weights are also provided. Weight shows how much influence the probe has
on the terrain, and is used when the blending between multiple reflection
probes occurs.  
[GetKeepUnusedCameraRenderingResources](Terrain.GetKeepUnusedCameraRenderingResources.html)|  
[GetPosition](Terrain.GetPosition.html)| Get the position of the terrain.  
[GetSplatMaterialPropertyBlock](Terrain.GetSplatMaterialPropertyBlock.html)|
Get the previously set splat material properties by copying to the dest
MaterialPropertyBlock object.  
[SampleHeight](Terrain.SampleHeight.html)| Samples the height at the given
position defined in world space, relative to the Terrain space.  
[SetKeepUnusedCameraRenderingResources](Terrain.SetKeepUnusedCameraRenderingResources.html)|
Defines whether Unity cleans up rendering resources for a given Camera during
garbage collection.  
[SetNeighbors](Terrain.SetNeighbors.html)| Lets you set up the connection
between neighboring Terrain tiles. This ensures LOD matches up on neighboring
Terrain tiles.  
[SetSplatMaterialPropertyBlock](Terrain.SetSplatMaterialPropertyBlock.html)|
Set the additional material properties when rendering the terrain heightmap
using the splat material.  
  
### Static Methods

[CreateTerrainGameObject](Terrain.CreateTerrainGameObject.html)| Creates a
Terrain including collider from TerrainData.  
---|---  
[GetActiveTerrains](Terrain.GetActiveTerrains.html)| Populates a List of
Terrains with the active Terrains in the Scene.  
[SetConnectivityDirty](Terrain.SetConnectivityDirty.html)| Marks the current
connectivity status as invalid.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
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

