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

#  [Collider](Collider.html).enabled

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

public bool enabled;

### Description

Enabled Colliders will collide with other Colliders, disabled Colliders won't.

This is shown as the small checkbox in the inspector of the Colliders. It
decides if a GameObject can collide with other Colliders.

    
    
    //This example enables and disables the [GameObject](GameObject.html)'s [Collider](Collider.html) when the space bar is pressed.
    //Attach this to a [GameObject](GameObject.html) and attach a [Collider](Collider.html) to the [GameObject](GameObject.html)  
      
    using UnityEngine;  
      
    public class ColliderEnabled : [MonoBehaviour](MonoBehaviour.html)
    {
        [Collider](Collider.html) m_Collider;  
      
        void Start()
        {
            //Fetch the [GameObject](GameObject.html)'s [Collider](Collider.html) (make sure it has a [Collider](Collider.html) component)
            m_Collider = GetComponent<[Collider](Collider.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                //[Toggle](UIElements.Toggle.html) the [Collider](Collider.html) on and off when pressing the space bar
                m_Collider.enabled = !m_Collider.enabled;  
      
                //Output to console whether the [Collider](Collider.html) is on or not
                [Debug.Log](Debug.Log.html)("[Collider.enabled](Collider-enabled.html) = " + m_Collider.enabled);
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

