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

# TerrainChangedFlags

enumeration

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

Indicate the types of changes to the terrain in OnTerrainChanged callback.

Use bitwise AND to detect multiple changes.

    
    
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class DetectTerrainChanges : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnTerrainChanged([TerrainChangedFlags](TerrainChangedFlags.html) flags)
        {
            if ((flags & [TerrainChangedFlags.Heightmap](TerrainChangedFlags.Heightmap.html)) != 0)
            {
                [Debug.Log](Debug.Log.html)("Heightmap changes");
            }  
      
            if ((flags & [TerrainChangedFlags.DelayedHeightmapUpdate](TerrainChangedFlags.DelayedHeightmapUpdate.html)) != 0)
            {
                [Debug.Log](Debug.Log.html)("Heightmap painting");
            }  
      
            if ((flags & [TerrainChangedFlags.TreeInstances](TerrainChangedFlags.TreeInstances.html)) != 0)
            {
                [Debug.Log](Debug.Log.html)("[Tree](Tree.html) changes");
            }
        }
    }
    

The above example shows how you can detect terrain changes by using
OnTerrainChanged callback and TerrainChangedFlags enum.

### Properties

[Heightmap](TerrainChangedFlags.Heightmap.html)| Indicates a change to the
heightmap data.  
---|---  
[TreeInstances](TerrainChangedFlags.TreeInstances.html)| Indicates a change to
the tree data.  
[DelayedHeightmapUpdate](TerrainChangedFlags.DelayedHeightmapUpdate.html)|
Indicates a change to the heightmap data without computing LOD.  
[FlushEverythingImmediately](TerrainChangedFlags.FlushEverythingImmediately.html)|
Indicates that a change was made to the terrain that was so significant that
the internal rendering data need to be flushed and recreated.  
[RemoveDirtyDetailsImmediately](TerrainChangedFlags.RemoveDirtyDetailsImmediately.html)|
Indicates a change to the detail data.  
[HeightmapResolution](TerrainChangedFlags.HeightmapResolution.html)| Indicates
a change to the heightmap resolution.  
[Holes](TerrainChangedFlags.Holes.html)| Indicates a change to the Terrain
holes data.  
[DelayedHolesUpdate](TerrainChangedFlags.DelayedHolesUpdate.html)| Indicates a
change to the Terrain holes data, which doesn't include LOD calculations and
tree/vegetation updates.  
[WillBeDestroyed](TerrainChangedFlags.WillBeDestroyed.html)| Indicates that
the TerrainData object is about to be destroyed.  
  
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

