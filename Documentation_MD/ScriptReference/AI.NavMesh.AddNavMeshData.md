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

#  [NavMesh](AI.NavMesh.html).AddNavMeshData

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

public static [AI.NavMeshDataInstance](AI.NavMeshDataInstance.html)
AddNavMeshData([AI.NavMeshData](AI.NavMeshData.html) navMeshData);

### Parameters

navMeshData | Contains the data for the navmesh.  
---|---  
  
### Returns

**NavMeshDataInstance** Representing the added navmesh.

### Description

Adds the specified NavMeshData to the game.

This makes the NavMesh data available for agents and NavMesh queries. Returns
an instance for later removing the NavMesh data from the runtime.  
  
The instance returned will be valid unless the NavMesh data could not be added
- e.g. due to running out of memory or navmesh data being loaded from a
corrupted file.  
  
Additional resources: [NavMeshDataInstance](AI.NavMeshDataInstance.html),
[RemoveNavMeshData](AI.NavMesh.RemoveNavMeshData.html).

* * *

## Declaration

public static [AI.NavMeshDataInstance](AI.NavMeshDataInstance.html)
AddNavMeshData([AI.NavMeshData](AI.NavMeshData.html) navMeshData,
[Vector3](Vector3.html) position, [Quaternion](Quaternion.html) rotation);

### Parameters

navMeshData | Contains the data for the navmesh.  
---|---  
position | Translate the navmesh to this position.  
rotation | Rotate the navmesh to this orientation.  
  
### Returns

**NavMeshDataInstance** Representing the added navmesh.

### Description

Adds the specified NavMeshData to the game.

This function is similar to [AddNavMeshData](AI.NavMesh.AddNavMeshData.html)
above, but the position and rotation specified is applied in addition to the
position and rotation where the NavMesh data was baked.

    
    
    using UnityEngine;
    using UnityEngine.AI;  
      
    class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [NavMeshData](AI.NavMeshData.html) data;
        [NavMeshDataInstance](AI.NavMeshDataInstance.html)[] instances = new [NavMeshDataInstance](AI.NavMeshDataInstance.html)[2];  
      
        public void OnEnable()
        {
            // Add an instance of navmesh data
            instances[0] = [NavMesh.AddNavMeshData](AI.NavMesh.AddNavMeshData.html)(data);  
      
            // Add another instance of the same navmesh data - displaced and rotated
            instances[1] = [NavMesh.AddNavMeshData](AI.NavMesh.AddNavMeshData.html)(data, new [Vector3](Vector3.html)(0, 5, 0), [Quaternion.AngleAxis](Quaternion.AngleAxis.html)(90, [Vector3.up](Vector3-up.html)));
        }  
      
        public void OnDisable()
        {
            instances[0].Remove();
            instances[1].Remove();
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

