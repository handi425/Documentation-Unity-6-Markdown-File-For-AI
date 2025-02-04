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

#  [NavMeshAgent](AI.NavMeshAgent.html).CalculatePath

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

public bool CalculatePath([Vector3](Vector3.html) targetPosition,
[AI.NavMeshPath](AI.NavMeshPath.html) path);

### Parameters

targetPosition | The final position of the path requested.  
---|---  
path | The resulting path.  
  
### Returns

**bool** True if either a complete or partial path is found. False otherwise.

### Description

Calculate a path to a specified point and store the resulting path.

Use this function to avoid gameplay delays by planning a path before it is
needed. You can also use this function to check if a target position is
reachable before moving the agent. The function takes into account the agent's
areaMask, agentTypeID and [area costs](AI.NavMeshAgent.GetAreaCost.html)
properties when it searches for a matching path.  
  
This function is synchronous. It performs path finding immediately, which can
adversely affect the frame rate when processing very long paths. It is
recommended to only perform a few path finds per frame when, for example,
evaluating distances to cover points.  
  
Use the returned path to set the path for this agent, or an agent of the same
type, with [NavMeshAgent.SetPath](AI.NavMeshAgent.SetPath.html). For SetPath
to work, the agent must be close to the starting point and be allowed to move
through the [area type](AI.NavMeshAgent-areaMask.html) where the start point
is.

    
    
    using UnityEngine;
    using UnityEngine.AI;  
      
    [[RequireComponent](RequireComponent.html)(typeof([NavMeshAgent](AI.NavMeshAgent.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;  
      
        void Start()
        {
            if (target == null)
                return;  
      
            var agent = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>();
            var path = new [NavMeshPath](AI.NavMeshPath.html)();
            agent.CalculatePath(target.position, path);
            switch (path.status)
            {
                case [NavMeshPathStatus.PathComplete](AI.NavMeshPathStatus.PathComplete.html):
                    [Debug.Log](Debug.Log.html)($"{agent.name} will be able to reach {target.name}.");
                    break;
                case [NavMeshPathStatus.PathPartial](AI.NavMeshPathStatus.PathPartial.html):
                    [Debug.LogWarning](Debug.LogWarning.html)($"{agent.name} will only be able to move partway to {target.name}.");
                    break;
                default:
                    [Debug.LogError](Debug.LogError.html)($"There is no valid path for {agent.name} to reach {target.name}.");
                    break;
            }
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

