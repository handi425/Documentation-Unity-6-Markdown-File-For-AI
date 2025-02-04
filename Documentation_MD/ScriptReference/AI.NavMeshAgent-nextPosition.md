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

#  [NavMeshAgent](AI.NavMeshAgent.html).nextPosition

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

public [Vector3](Vector3.html) nextPosition;

### Description

Gets or sets the simulation position of the navmesh agent.

The position vector is in world space coordinates and units.  
  
The nextPosition is coupled to [Transform.position](Transform-position.html).
In the default case the navmesh agent's Transform position will match the
internal simulation position at the time the script Update function is called.
This coupling can be turned on and off by setting
[updatePosition](AI.NavMeshAgent-updatePosition.html).  
  
When [updatePosition](AI.NavMeshAgent-updatePosition.html) is true, the
[Transform.position](Transform-position.html) reflects the simulated position,
when false the position of the transform and the navmesh agent is not
synchronized, and you'll see a difference between the two in general. When
[updatePosition](AI.NavMeshAgent-updatePosition.html) is turned back on, the
[Transform.position](Transform-position.html) will be immediately move to
match nextPosition.  
  
By setting nextPosition you can directly control where the internal agent
position should be. The agent will be moved towards the position, but is
constrained by the navmesh connectivity and boundaries. As such it will be
useful only if the positions are continuously updated and assessed. Additional
resources: [Warp](AI.NavMeshAgent.Warp.html) for teleporting a navmesh agent.

    
    
    using UnityEngine;
    using UnityEngine.AI;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // [Update](PlayerLoop.Update.html) the transform position explicitly in the OnAnimatorMove callback
            GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>().updatePosition = false;
        }  
      
        void OnAnimatorMove()
        {
            transform.position = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>().nextPosition;
        }
    }
    

Additionally it can be useful to control the agent position directly -
especially if the GO transform is controlled by something else - e.g.
animator, physics, scripted or input.

    
    
    using UnityEngine;
    using UnityEngine.AI;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public bool agentIsControlledByOther;
        void [Update](PlayerLoop.Update.html)()
        {
            var agent = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>();
            agent.updatePosition = !agentIsControlledByOther;
            if (agentIsControlledByOther)
            {
                GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>().nextPosition = transform.position;
            }
        }
    }
    

Additional resources: [Move](AI.NavMeshAgent.Move.html) for moving the agent
with a relative position.

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

