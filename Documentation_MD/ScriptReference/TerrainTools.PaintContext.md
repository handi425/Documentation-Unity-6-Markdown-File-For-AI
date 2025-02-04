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

# PaintContext

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

The context for a paint operation that may span multiple connected Terrain
tiles.

This class is used to apply an edit operation to an area of Terrain that may
span multiple Terrain tiles. A PaintContext may be used to edit heightmap or
splatmap data, and may also be used to gather normal data in read-only mode
(you cannot write to normals, because they are derived from the heightmap).  
  
A PaintContext will calculate the relevant regions on each Terrain, and
collect the original data into a single sourceRenderTarget. Your edit
operation can then read from sourcerenderTarget, and write the modified data
to destinationRenderTarget. Once you have applied your edit operation, the
PaintContext can also write the modified data in destinationRenderTarget back
to each Terrain, ensuring no seams between them.  
  
The simplest way to use a PaintContext is through the helper functions in
TerrainPaintUtility:  
[TerrainPaintUtility.BeginPaintHeightmap](TerrainTools.TerrainPaintUtility.BeginPaintHeightmap.html),
[TerrainPaintUtility.EndPaintHeightmap](TerrainTools.TerrainPaintUtility.EndPaintHeightmap.html),
[TerrainPaintUtility.BeginPaintTexture](TerrainTools.TerrainPaintUtility.BeginPaintTexture.html),
[TerrainPaintUtility.EndPaintTexture](TerrainTools.TerrainPaintUtility.EndPaintTexture.html),
[TerrainPaintUtility.CollectNormals](TerrainTools.TerrainPaintUtility.CollectNormals.html)
and
[TerrainPaintUtility.ReleaseContextResources](TerrainTools.TerrainPaintUtility.ReleaseContextResources.html).  
  
You can also use PaintContext more directly through its member functions. In
general, they are used in the following order:  
1) Constructor,
[PaintContext.CreateFromBounds](TerrainTools.PaintContext.CreateFromBounds.html)
\- Construct a PaintContext with a target Terrain and a region to edit  
2)
[PaintContext.CreateRenderTargets](TerrainTools.PaintContext.CreateRenderTargets.html)
\- Create the source and destination RenderTargets  
3)
[PaintContext.GatherHeightmap](TerrainTools.PaintContext.GatherHeightmap.html),
[PaintContext.GatherAlphamap](TerrainTools.PaintContext.GatherAlphamap.html),
[PaintContext.GatherNormals](TerrainTools.PaintContext.GatherNormals.html) \-
Read from Terrain tiles into sourceRenderTarget  
4) Apply editing operations, reading from sourceRenderTarget, and writing to
destinationRenderTarget  
5)
[PaintContext.ScatterHeightmap](TerrainTools.PaintContext.ScatterHeightmap.html),
[PaintContext.ScatterAlphamap](TerrainTools.PaintContext.ScatterAlphamap.html)
\- Write from destinationRenderTarget into Terrain tiles (optional)  
6) [PaintContext.Cleanup](TerrainTools.PaintContext.Cleanup.html) \- Destroy
RenderTarget resources (required if you call CreateRenderTargets)  
7)
[PaintContext.ApplyDelayedActions](TerrainTools.PaintContext.ApplyDelayedActions.html)
\- Apply any delayed actions that perform expensive updates  
  
  
Additional resources:
[TerrainPaintTool<T0>](TerrainTools.TerrainPaintTool_1.html)

### Static Properties

[kNormalizedHeightScale](TerrainTools.PaintContext-
kNormalizedHeightScale.html)| Unity uses this value internally to transform a
[0, 1] height value to a texel value, which is stored in
TerrainData.heightmapTexture.  
---|---  
  
### Properties

[destinationRenderTexture](TerrainTools.PaintContext-
destinationRenderTexture.html)| (Read Only) RenderTexture that an edit
operation writes to modify the data.  
---|---  
[heightWorldSpaceMin](TerrainTools.PaintContext-heightWorldSpaceMin.html)| The
minimum height of all Terrain tiles that this PaintContext touches in world
space.  
[heightWorldSpaceSize](TerrainTools.PaintContext-heightWorldSpaceSize.html)|
The height range (from Min to Max) of all Terrain tiles that this PaintContext
touches in world space.  
[oldRenderTexture](TerrainTools.PaintContext-oldRenderTexture.html)| (Read
Only) The value of RenderTexture.active at the time CreateRenderTargets is
called.  
[originTerrain](TerrainTools.PaintContext-originTerrain.html)| (Read Only) The
Terrain used to build the PaintContext.  
[pixelRect](TerrainTools.PaintContext-pixelRect.html)| (Read Only) The pixel
rectangle that this PaintContext represents.  
[pixelSize](TerrainTools.PaintContext-pixelSize.html)| (Read Only) The size of
a PaintContext pixel in terrain units (as defined by originTerrain.)  
[sourceRenderTexture](TerrainTools.PaintContext-sourceRenderTexture.html)|
(Read Only) Render target that stores the original data from the Terrain
tiles.  
[targetTextureHeight](TerrainTools.PaintContext-targetTextureHeight.html)|
(Read Only) The height of the target terrain texture. This is the resolution
for a single Terrain.  
[targetTextureWidth](TerrainTools.PaintContext-targetTextureWidth.html)| (Read
Only) The width of the target terrain texture. This is the resolution for a
single Terrain.  
[terrainCount](TerrainTools.PaintContext-terrainCount.html)| (Read Only) The
number of Terrain tiles in this PaintContext.  
  
### Constructors

[PaintContext](TerrainTools.PaintContext-ctor.html)| Creates a new
PaintContext, to edit a target texture on a Terrain, in a region defined by
pixelRect.  
---|---  
  
### Public Methods

[Cleanup](TerrainTools.PaintContext.Cleanup.html)| Releases the allocated
resources of this PaintContext.  
---|---  
[CreateRenderTargets](TerrainTools.PaintContext.CreateRenderTargets.html)|
Creates the sourceRenderTexture and destinationRenderTexture.  
[Gather](TerrainTools.PaintContext.Gather.html)| Gathers user-specified
Texture data into sourceRenderTexture.  
[GatherAlphamap](TerrainTools.PaintContext.GatherAlphamap.html)| Gathers the
alphamap information into sourceRenderTexture.  
[GatherHeightmap](TerrainTools.PaintContext.GatherHeightmap.html)| Gathers the
heightmap information into sourceRenderTexture.  
[GatherHoles](TerrainTools.PaintContext.GatherHoles.html)| Gathers the Terrain
holes information into sourceRenderTexture.  
[GatherNormals](TerrainTools.PaintContext.GatherNormals.html)| Gathers the
normal information into sourceRenderTexture.  
[GetClippedPixelRectInRenderTexturePixels](TerrainTools.PaintContext.GetClippedPixelRectInRenderTexturePixels.html)|
Retrieves the clipped pixel rectangle for a Terrain, relative to the
PaintContext render textures.  
[GetClippedPixelRectInTerrainPixels](TerrainTools.PaintContext.GetClippedPixelRectInTerrainPixels.html)|
Retrieves the clipped pixel rectangle for a Terrain.  
[GetTerrain](TerrainTools.PaintContext.GetTerrain.html)| Retrieves a Terrain
from the PaintContext.  
[Scatter](TerrainTools.PaintContext.Scatter.html)| Applies an edited
PaintContext by copying modifications back to user-specified RenderTextures
for the source Terrain tiles.  
[ScatterAlphamap](TerrainTools.PaintContext.ScatterAlphamap.html)| Applies an
edited alphamap PaintContext by copying modifications back to the source
Terrain tiles.  
[ScatterHeightmap](TerrainTools.PaintContext.ScatterHeightmap.html)| Applies
an edited heightmap PaintContext by copying modifications back to the source
Terrain tiles.  
[ScatterHoles](TerrainTools.PaintContext.ScatterHoles.html)| Applies an edited
Terrain holes PaintContext by copying modifications back to the source Terrain
tiles.  
  
### Static Methods

[ApplyDelayedActions](TerrainTools.PaintContext.ApplyDelayedActions.html)|
Flushes the delayed actions created by PaintContext heightmap and alphamap
modifications.  
---|---  
[CreateFromBounds](TerrainTools.PaintContext.CreateFromBounds.html)|
Constructs a PaintContext that you can use to edit a texture on a Terrain, in
the region defined by boundsInTerrainSpace and extraBorderPixels.  
  
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

