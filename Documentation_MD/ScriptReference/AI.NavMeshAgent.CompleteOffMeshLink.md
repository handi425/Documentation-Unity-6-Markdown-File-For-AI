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

#  [NavMeshAgent](AI.NavMeshAgent.html).CompleteOffMeshLink

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

public void CompleteOffMeshLink();

### Description

Completes the movement on the current OffMeshLink.

The agent will move to the closest valid navmesh position on the other end of
the current OffMeshLink.  
  
CompleteOffMeshLink has no effect unless the agent is on an OffMeshLink
(Additional resources: [isOnOffMeshLink](AI.NavMeshAgent-
isOnOffMeshLink.html)).  
  
When [autoTraverseOffMeshLink](AI.NavMeshAgent-autoTraverseOffMeshLink.html)
is disabled an agent will pause at an off-mesh link until this function is
called. It is useful for implementing custom movement across OffMeshLinks.

    
    
    using UnityEngine;
    using UnityEngine.AI;
    using System.Collections;  
      
    public enum OffMeshLinkMoveMethod
    {
        Teleport,
        NormalSpeed,
        Parabola
    }  
      
    [[RequireComponent](RequireComponent.html)(typeof([NavMeshAgent](AI.NavMeshAgent.html)))]
    public class AgentLinkMover : [MonoBehaviour](MonoBehaviour.html)
    {
        public OffMeshLinkMoveMethod method = OffMeshLinkMoveMethod.Parabola;
        IEnumerator Start()
        {
            [NavMeshAgent](AI.NavMeshAgent.html) agent = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>();
            agent.autoTraverseOffMeshLink = false;
            while (true)
            {
                if (agent.isOnOffMeshLink)
                {
                    if (method == OffMeshLinkMoveMethod.NormalSpeed)
                        yield return StartCoroutine(NormalSpeed(agent));
                    else if (method == OffMeshLinkMoveMethod.Parabola)
                        yield return StartCoroutine(Parabola(agent, 2.0f, 0.5f));
                    agent.CompleteOffMeshLink();
                }
                yield return null;
            }
        }  
      
        IEnumerator NormalSpeed([NavMeshAgent](AI.NavMeshAgent.html) agent)
        {
            [OffMeshLinkData](AI.OffMeshLinkData.html) data = agent.currentOffMeshLinkData;
            [Vector3](Vector3.html) endPos = data.endPos + [Vector3.up](Vector3-up.html) * agent.baseOffset;
            while (agent.transform.position != endPos)
            {
                agent.transform.position = [Vector3.MoveTowards](Vector3.MoveTowards.html)(agent.transform.position, endPos, agent.speed * [Time.deltaTime](Time-deltaTime.html));
                yield return null;
            }
        }  
      
        IEnumerator Parabola([NavMeshAgent](AI.NavMeshAgent.html) agent, float height, float duration)
        {
            [OffMeshLinkData](AI.OffMeshLinkData.html) data = agent.currentOffMeshLinkData;
            [Vector3](Vector3.html) startPos = agent.transform.position;
            [Vector3](Vector3.html) endPos = data.endPos + [Vector3.up](Vector3-up.html) * agent.baseOffset;
            float normalizedTime = 0.0f;
            while (normalizedTime < 1.0f)
            {
                float yOffset = height * 4.0f * (normalizedTime - normalizedTime * normalizedTime);
                agent.transform.position = [Vector3.Lerp](Vector3.Lerp.html)(startPos, endPos, normalizedTime) + yOffset * [Vector3.up](Vector3-up.html);
                normalizedTime += [Time.deltaTime](Time-deltaTime.html) / duration;
                yield return null;
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

