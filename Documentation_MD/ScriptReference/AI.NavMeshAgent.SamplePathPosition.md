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

#  [NavMeshAgent](AI.NavMeshAgent.html).SamplePathPosition

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

public bool SamplePathPosition(int areaMask, float maxDistance, out
[AI.NavMeshHit](AI.NavMeshHit.html) hit);

### Parameters

areaMask | A bitfield mask specifying which NavMesh areas can be passed when tracing the path.  
---|---  
maxDistance | Terminate scanning the path at this distance.  
hit | Holds the properties of the resulting location.  
  
### Returns

**bool** True if terminated before reaching the position at maxDistance, false
otherwise.

### Description

Sample a position along the current path.

This function looks ahead a specified distance along the current path. Details
of the mesh at that position are then returned in a
[NavMeshHit](AI.NavMeshHit.html) object. This could be used, for example, to
check the type of surface that lies ahead before the character gets there - a
character could raise his gun above his head if he is about to wade through
water, say.

    
    
    using UnityEngine;
    using UnityEngine.AI;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;
        private [NavMeshAgent](AI.NavMeshAgent.html) agent;
        private int waterMask;  
      
    
        void Start()
        {
            agent = GetComponent<[NavMeshAgent](AI.NavMeshAgent.html)>();
            waterMask = 1 << [NavMesh.GetAreaFromName](AI.NavMesh.GetAreaFromName.html)("Water");
            agent.SetDestination(target.position);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [NavMeshHit](AI.NavMeshHit.html) hit;  
      
            // Check all areas one length unit ahead.
            if (!agent.SamplePathPosition([NavMesh.AllAreas](AI.NavMesh.AllAreas.html), 1.0F, out hit))
                if ((hit.mask & waterMask) != 0)
                {
                    // Water detected along the path...
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

