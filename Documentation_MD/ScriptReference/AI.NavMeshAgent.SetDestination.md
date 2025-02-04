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

#  [NavMeshAgent](AI.NavMeshAgent.html).SetDestination

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

public bool SetDestination([Vector3](Vector3.html) target);

### Parameters

target | The target point to navigate to.  
---|---  
  
### Returns

**bool** True if the destination was requested successfully, otherwise false.

### Description

Sets or updates the destination thus triggering the calculation for a new
path.

Note that the path may not become available until after a few frames later.
While the path is being computed, [pathPending](AI.NavMeshAgent-
pathPending.html) will be true. If a valid path becomes available then the
agent will resume movement.

    
    
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [NavMeshAgent](AI.NavMeshAgent.html) myNavMeshAgent;
        void Start()
        {
            myNavMeshAgent = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetMouseButtonDown](Input.GetMouseButtonDown.html)(0))
            {
                SetDestinationToMousePosition();
            }
        }  
      
        void SetDestinationToMousePosition()
        {
            [RaycastHit](RaycastHit.html) hit;
            [Ray](Ray.html) ray = Camera.main.ScreenPointToRay([Input.mousePosition](Input-mousePosition.html));
            if ([Physics.Raycast](Physics.Raycast.html)(ray, out hit))
            {
                myNavMeshAgent.SetDestination(hit.point);
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

