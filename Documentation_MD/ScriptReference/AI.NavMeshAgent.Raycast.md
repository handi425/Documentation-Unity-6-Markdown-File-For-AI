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

#  [NavMeshAgent](AI.NavMeshAgent.html).Raycast

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

public bool Raycast([Vector3](Vector3.html) targetPosition, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit);

### Parameters

targetPosition | The desired end position of movement.  
---|---  
hit | Properties of the obstacle detected by the ray (if any).  
  
### Returns

**bool** True if there is an obstacle between the agent and the target
position, otherwise false.

### Description

Trace a straight path towards a target postion in the NavMesh without moving
the agent.

This function follows the path of a "ray" between the agent's position and the
specified target position. If an obstruction is encountered along the line
then a true value is returned and the position and other details of the
obstructing object are stored in the `hit` parameter. This can be used to
check if there is a clear shot or line of sight between a character and a
target object. This function is preferable to the similar
[Physics.Raycast](Physics.Raycast.html) because the line tracing is performed
in a simpler way using the navmesh and has a lower processing overhead.

    
    
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        private [NavMeshAgent](AI.NavMeshAgent.html) agent;  
      
        void Start()
        {
            agent = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [NavMeshHit](AI.NavMeshHit.html) hit;
            if (!agent.Raycast(target.position, out hit))
            {
                // [Target](GraphicsBuffer.Target.html) is "visible" from our position.
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

