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

#  [NavMeshEditorHelpers](AI.NavMeshEditorHelpers.html).DrawBuildDebug

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

public static void DrawBuildDebug([AI.NavMeshData](AI.NavMeshData.html)
navMeshData, [AI.NavMeshBuildDebugFlags](AI.NavMeshBuildDebugFlags.html) flags
= NavMeshBuildDebugFlags.All);

### Parameters

navMeshData | NavMesh object for which debug data has been deliberately collected during the build process.  
---|---  
flags | Bitmask that designates the types of data to show at one time.  
  
### Description

Displays in the Editor the precise intermediate data used during the build
process of the specified NavMesh.

Additional resources: [NavMeshBuildSettings.debug](AI.NavMeshBuildSettings-
debug.html).

    
    
    using System.Collections.Generic;
    using UnityEditor.AI;
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class NavMeshBuildDebugDraw : [MonoBehaviour](MonoBehaviour.html)
    {
        [NavMeshData](AI.NavMeshData.html) m_NavMeshData;  
      
        void Start()
        {
            var bounds = new [Bounds](Bounds.html)(transform.position, new [Vector3](Vector3.html)(100.0f, 100.0f, 100.0f));
            var markups = new List<[NavMeshBuildMarkup](AI.NavMeshBuildMarkup.html)>();
            var sources = new List<[NavMeshBuildSource](AI.NavMeshBuildSource.html)>();
            [NavMeshEditorHelpers.CollectSourcesInStage](AI.NavMeshEditorHelpers.CollectSourcesInStage.html)(
                bounds, ~0, [NavMeshCollectGeometry.RenderMeshes](AI.NavMeshCollectGeometry.RenderMeshes.html), 0, markups, gameObject.scene, sources);  
      
            var settings = [NavMesh.GetSettingsByID](AI.NavMesh.GetSettingsByID.html)(0);
            var debug = new [NavMeshBuildDebugSettings](AI.NavMeshBuildDebugSettings.html)();
            debug.flags = [NavMeshBuildDebugFlags.All](AI.NavMeshBuildDebugFlags.All.html);
            settings.debug = debug;  
      
            m_NavMeshData = new [NavMeshData](AI.NavMeshData.html)();
            UnityEngine.AI.NavMeshBuilder.UpdateNavMeshDataAsync(m_NavMeshData, settings, sources, bounds);
        }  
      
        void OnDrawGizmos()
        {
            [NavMeshEditorHelpers.DrawBuildDebug](AI.NavMeshEditorHelpers.DrawBuildDebug.html)(
                m_NavMeshData, [NavMeshBuildDebugFlags.Regions](AI.NavMeshBuildDebugFlags.Regions.html) | [NavMeshBuildDebugFlags.SimplifiedContours](AI.NavMeshBuildDebugFlags.SimplifiedContours.html));
        }
    }
    

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

