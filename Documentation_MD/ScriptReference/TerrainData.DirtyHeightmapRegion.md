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

#  [TerrainData](TerrainData.html).DirtyHeightmapRegion

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

public void DirtyHeightmapRegion([RectInt](RectInt.html) region,
[TerrainHeightmapSyncControl](TerrainHeightmapSyncControl.html) syncControl);

### Parameters

region | The rectangular region to mark as dirty.  
---|---  
syncControl | Controls how CPU synchronization is performed.  
  
### Description

Marks the specified part of the heightmap as dirty.

Use this function only after you manually change the GPU part of the heightmap
texture by rendering into it, or by using
[Graphics.CopyTexture](Graphics.CopyTexture.html). Use the `syncControl`
parameter to control how you want Unity to perform CPU synchronization. Unity
queues the reading back of unsynchronized data (height data, LOD data, or
both) until the next call to [SyncHeightmap](TerrainData.SyncHeightmap.html).  
  
If the current active [RenderTexture](RenderTexture.html) contains your
changes, and you want to copy a part of it into the heightmap texture, use
[CopyActiveRenderTextureToHeightmap](TerrainData.CopyActiveRenderTextureToHeightmap.html)
instead.  
  
This function sends out the OnTerrainChanged message with
[TerrainChangedFlags.Heightmap](TerrainChangedFlags.Heightmap.html) if you
pass
[TerrainHeightmapSyncControl.HeightAndLod](TerrainHeightmapSyncControl.HeightAndLod.html)
to the `syncControl` parameter. If you pass
[TerrainHeightmapSyncControl.Height](TerrainHeightmapSyncControl.Height.html)
to the `syncControl` parameter, it sends out the OnTerrainChanged message with
[TerrainChangedFlags.DelayedHeightmapUpdate](TerrainChangedFlags.DelayedHeightmapUpdate.html).

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

