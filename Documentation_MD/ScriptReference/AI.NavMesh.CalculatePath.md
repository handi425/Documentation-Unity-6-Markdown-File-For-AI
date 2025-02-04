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

#  [NavMesh](AI.NavMesh.html).CalculatePath

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

public static bool CalculatePath([Vector3](Vector3.html) sourcePosition,
[Vector3](Vector3.html) targetPosition, int areaMask,
[AI.NavMeshPath](AI.NavMeshPath.html) path);

### Parameters

sourcePosition | The initial position of the path requested.  
---|---  
targetPosition | The final position of the path requested.  
areaMask | A bitfield mask specifying which NavMesh areas can be passed when calculating a path.  
path | The resulting path.  
  
### Returns

**bool** True if either a complete or partial path is found. False otherwise.

### Description

Calculate a path between two points and store the resulting path.

Use this function to avoid gameplay delays by planning a path before it is
needed. You can also use this function to check if a target position is
reachable before moving the agent.  
  
This function is synchronous. It performs path finding immediately which can
adversely affect the frame rate when processing very long paths. It is
recommended to only perform a few path finds per frame when, for example,
evaluating distances to cover points.  
  
Use the returned path to set the path for an agent with
[NavMeshAgent.SetPath](AI.NavMeshAgent.SetPath.html). For SetPath to work, the
agent must be close to the starting point.

    
    
    // ShowGoldenPath
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class ShowGoldenPath : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        private [NavMeshPath](AI.NavMeshPath.html) path;
        private float elapsed = 0.0f;
        void Start()
        {
            path = new [NavMeshPath](AI.NavMeshPath.html)();
            elapsed = 0.0f;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // [Update](PlayerLoop.Update.html) the way to the goal every second.
            elapsed += [Time.deltaTime](Time-deltaTime.html);
            if (elapsed > 1.0f)
            {
                elapsed -= 1.0f;
                [NavMesh.CalculatePath](AI.NavMesh.CalculatePath.html)(transform.position, target.position, [NavMesh.AllAreas](AI.NavMesh.AllAreas.html), path);
            }
            for (int i = 0; i < path.corners.Length - 1; i++)
                [Debug.DrawLine](Debug.DrawLine.html)(path.corners[i], path.corners[i + 1], [Color.red](Color-red.html));
        }
    }
    

* * *

## Declaration

public static bool CalculatePath([Vector3](Vector3.html) sourcePosition,
[Vector3](Vector3.html) targetPosition,
[AI.NavMeshQueryFilter](AI.NavMeshQueryFilter.html) filter,
[AI.NavMeshPath](AI.NavMeshPath.html) path);

### Parameters

sourcePosition | The initial position of the path requested.  
---|---  
targetPosition | The final position of the path requested.  
filter | A filter specifying the cost of NavMesh areas that can be passed when calculating a path.  
path | The resulting path.  
  
### Returns

**bool** True if a either a complete or partial path is found and false
otherwise.

### Description

Calculates a path between two positions mapped to the NavMesh, subject to the
constraints and costs defined by the filter argument.

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

