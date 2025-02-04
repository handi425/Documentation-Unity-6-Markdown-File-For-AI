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

#  [NavMeshAgent](AI.NavMeshAgent.html).destination

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

public [Vector3](Vector3.html) destination;

### Description

Gets or attempts to set the destination of the agent in world-space units.

Getting:  
  
Returns the destination set for this agent.  
  
• If a destination is set but the path is not yet processed the position
returned will be valid navmesh position that's closest to the previously set
position.  
• If the agent has no path or requested path - returns the agents position on
the navmesh.  
• If the agent is not mapped to the navmesh (e.g. Scene has no navmesh) -
returns a position at infinity.  
  
Setting:  
  
Requests the agent to move to the valid navmesh position that's closest to the
requested destination.  
  
• The path result may not become available until after a few frames. Use
[pathPending](AI.NavMeshAgent-pathPending.html) to query for outstanding
results.  
• If it's not possible to find a valid nearby navmesh position (e.g. Scene has
no navmesh) no path is requested. Use
[SetDestination](AI.NavMeshAgent.SetDestination.html) and check return value
if you need to handle this case explicitly.

    
    
    using UnityEngine;
    using UnityEngine.AI;  
      
    [[RequireComponent](RequireComponent.html)(typeof([NavMeshAgent](AI.NavMeshAgent.html)))]
    public class FollowTarget : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        [Vector3](Vector3.html) destination;
        [NavMeshAgent](AI.NavMeshAgent.html) agent;  
      
        void Start()
        {
            // [Cache](Cache.html) agent component and destination
            agent = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>();
            destination = agent.destination;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // [Update](PlayerLoop.Update.html) destination if the target moves one unit
            if ([Vector3.Distance](Vector3.Distance.html)(destination, target.position) > 1.0f)
            {
                destination = target.position;
                agent.destination = destination;
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

