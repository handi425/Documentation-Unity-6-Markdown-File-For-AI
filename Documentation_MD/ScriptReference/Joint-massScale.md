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

#  [Joint](Joint.html).massScale

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

public float massScale;

### Description

The scale to apply to the inverse mass and inertia tensor of the body prior to
solving the constraints.

Scale mass and the inertia tensor to make the joints solver converge faster,
thus resulting in less stretch of the limbs of a typical ragdoll. Most useful
in conjunction with [Joint.connectedMassScale](Joint-connectedMassScale.html).  
  
For example, if you have two objects in a ragdoll of masses 1 and 10, the
physics engine will typically resolve the joint by changing the velocity of
the lighter body much more than the heavier one. Applying a mass scale of 10
to the first body makes solver change the velocity of both bodies by an equal
amount. Applying mass scales such that the joint sees similar effective masses
and inertias makes the solver converge faster, which can make individual
joints seem less rubbery or separated, and sets of jointed bodies appear less
twitchy  
  
Note that scaling mass and inertia is fundamentally nonphysical and momentum
won't be conserved.  
  
The following script is useful to adjust the mass and inertia scaling in order
to get the same corrective velocity out of the solver. Attach it to the
ragdoll's root, or to a limb that is over-stretched during the gameplay and it
will find all joints down in the transform hierarchy below itself and adjust
the mass scale.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class NormalizeMass : [MonoBehaviour](MonoBehaviour.html)
    {
        private void Apply([Transform](Transform.html) root)
        {
            var j = root.GetComponent<[Joint](Joint.html)>();  
      
            // Apply the inertia scaling if possible
            if (j && j.connectedBody)
            {
                // Make sure that both of the connected bodies will be moved by the solver with equal speed
                j.massScale = j.connectedBody.mass / root.GetComponent<[Rigidbody](Rigidbody.html)>().mass;
                j.connectedMassScale = 1f;
            }  
      
            // Continue for all children...
            for (int childId = 0; childId < root.childCount; ++childId)
            {
                Apply(root.GetChild(childId));
            }
        }  
      
        public void Start()
        {
            Apply(this.transform);
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

