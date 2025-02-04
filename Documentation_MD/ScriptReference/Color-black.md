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

#  [Color](Color.html).black

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

public static [Color](Color.html) black;

### Description

Solid black. RGBA is (0, 0, 0, 1).

    
    
    //Attach this script to a [GameObject](GameObject.html) with a [Renderer](Renderer.html) (go to **Create** >**3D Object** and select one of the first 6 options to create a [GameObject](GameObject.html) with a [Renderer](Renderer.html) automatically attached).
    //This script changes the [Color](Color.html) of your [GameObject](GameObject.html)’s [Material](Material.html) when your mouse hovers over it in Play [Mode](Scripting.GarbageCollector.Mode.html).  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Renderer](Renderer.html) m_Renderer;  
      
        void Start()
        {
            //Fetch the [Renderer](Renderer.html) component of the [GameObject](GameObject.html)
            m_Renderer = GetComponent<[Renderer](Renderer.html)>();
        }  
      
        //Run your mouse over the [GameObject](GameObject.html) to change the [Renderer](Renderer.html)'s material color to black
        void OnMouseOver()
        {
            m_Renderer.material.color = [Color.black](Color-black.html);
        }  
      
        //Change the [Material](Material.html)'s [Color](Color.html) back to white when the mouse exits the [GameObject](GameObject.html)
        void OnMouseExit()
        {
            m_Renderer.material.color = [Color.white](Color-white.html);
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

