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

#  [Vector3](Vector3.html).Set

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

public void Set(float newX, float newY, float newZ);

### Description

Set x, y and z components of an existing Vector3.

    
    
    // Attach this script to a [GameObject](GameObject.html). Create an empty [GameObject](GameObject.html) that will act as your "New [Transform](Transform.html)". Assign this in the Inspector.
    // Press the "Set" button in the game to set the [GameObject](GameObject.html)'s position to the "New [Transform](Transform.html)" position.  
      
    using UnityEngine;
    using UnityEngine.EventSystems;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Use this to set the new position of the [GameObject](GameObject.html)
        [Vector3](Vector3.html) m_MyPosition;  
      
        // Set an external [Transform](Transform.html) in the Inspector which is the [GameObject](GameObject.html)’s starting point
        public [Transform](Transform.html) m_NewTransform;  
      
        void Start()
        {
            // Set the new Vector to be that of the [Transform](Transform.html) you attach in the Inspector
            m_MyPosition.Set(m_NewTransform.position.x, m_NewTransform.position.y, 0);
        }  
      
        void OnGUI()
        {
            // Press the [Button](UIElements.Button.html) to set the [GameObject](GameObject.html) to this new position
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 0, 100, 40), "Set"))
            {
                transform.position = m_MyPosition;
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

