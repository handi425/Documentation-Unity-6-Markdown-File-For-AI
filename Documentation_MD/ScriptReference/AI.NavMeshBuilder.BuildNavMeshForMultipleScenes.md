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

**Method group is Obsolete**  

#  [NavMeshBuilder](AI.NavMeshBuilder.html).BuildNavMeshForMultipleScenes

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

**Obsolete** UnityEditor NavMeshBuilder has been deprecated. Use
UnityEngine.AI.NavMeshBuilder instead.

## Declaration

public static void BuildNavMeshForMultipleScenes(string[] paths);

### Parameters

paths | Array of paths to Scenes that are used for building the navmesh.  
---|---  
  
### Description

Builds the combined NavMesh for the contents of multiple Scenes.

Loads all the Scenes by path and then builds the combined navmesh data.  
  
The resulting navmesh data is stored in a single file. The navmesh file path
is identical to the default path for the first Scene in the array – e.g.
"Assets/Scene1/NavMesh.asset".  
  
The navmesh data is shared between all the Scenes specified.  
  
Note that your current Scene will be saved before, and restored after, the
build process. Additionally all Scenes passed to this method will be saved in
order to reference the combined navmesh data.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class BuildNavMeshFor3Scenes
    {
        [[MenuItem](MenuItem.html)("[NavMesh](AI.NavMesh.html)/BuildNavMeshFor3Scenes")]
        public static void Build()
        {
            string[] sceneNames = { "Assets/Scene1.unity", "Assets/Scene2.unity", "Assets/Scene3.unity" };
            UnityEditor.AI.NavMeshBuilder.BuildNavMeshForMultipleScenes(sceneNames);
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

