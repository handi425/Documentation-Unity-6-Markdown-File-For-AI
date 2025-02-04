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

#  [Cloth](Cloth.html).ClearTransformMotion

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

[Switch to Manual](../Manual/class-Cloth.html "Go to Cloth Component in the
Manual")

## Declaration

public void ClearTransformMotion();

### Description

Clear the pending transform changes from affecting the cloth simulation.

When the transform of a cloth changes, the cloth will not directly follow that
change, but instead, the new positions of the SkinnedMeshRenderer's vertices
will affect the cloth through the configured constraints in the next cloth
simulation update, so that moving the tranform will result in realistic motion
of the cloth.  
  
You can call ClearTransformMotion on the cloth to change this behavior.
Calling ClearTransformMotion will move the cloth simulation particles along
with the transform, so that the transform movement has no effect on the cloth
simulation. This is useful if you want to teleport Characters from one point
in the Scene to another, without having the cloth suddenly jerk into place.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Vector3](Vector3.html) newPosition;  
      
        void Start()
        {
            transform.position = newPosition;
            GetComponent<[Cloth](Cloth.html)>().ClearTransformMotion();
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

