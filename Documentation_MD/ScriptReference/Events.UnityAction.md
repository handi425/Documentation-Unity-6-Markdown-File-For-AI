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

# UnityAction

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

public delegate void UnityAction();

### Description

Zero argument delegate used by UnityEvents.

Use this to create some dynamic functionality in your scripts. Unity Actions
allow you to dynamically call multiple functions. Since Unity Actions have no
arguments, functions they call must also have no arguments. See [Delegates
](https://unity3d.com/learn/tutorials/topics/scripting/delegates) for more
information.

    
    
    //Attach this script to a [GameObject](GameObject.html). Attach a [Renderer](Renderer.html) and [Button](UIElements.Button.html) component to the same [GameObject](GameObject.html) for this example.
    //This script will change the [Color](Color.html) of the [GameObject](GameObject.html) as well as output messages to the Console saying which function was run by the [UnityAction](Events.UnityAction.html).  
      
    using UnityEngine;
    using UnityEngine.UI;
    using UnityEngine.Events;  
      
    public class UnityActionExample : [MonoBehaviour](MonoBehaviour.html)
    {
        //This is the [Button](UIElements.Button.html) you attach to the [GameObject](GameObject.html) in the Inspector
        [Button](UIElements.Button.html) m_AddButton;
        [Renderer](Renderer.html) m_Renderer;  
      
        private [UnityAction](Events.UnityAction.html) m_MyFirstAction;
        //This is the number that the script updates
        float m_MyNumber;  
      
        void Start()
        {
            //Fetch the [Button](UIElements.Button.html) and [Renderer](Renderer.html) components from the [GameObject](GameObject.html)
            m_AddButton = GetComponent<[Button](UIElements.Button.html)>();
            m_Renderer = GetComponent<[Renderer](Renderer.html)>();  
      
            //Make a Unity [Action](Unity.Android.Gradle.Manifest.Action.html) that calls your function
            m_MyFirstAction += MyFunction;
            //Make the Unity [Action](Unity.Android.Gradle.Manifest.Action.html) also call your second function
            m_MyFirstAction += MySecondFunction;
            //Register the [Button](UIElements.Button.html) to detect clicks and call your Unity [Action](Unity.Android.Gradle.Manifest.Action.html)
            m_AddButton.onClick.AddListener(m_MyFirstAction);
        }  
      
        void MyFunction()
        {
            //Add to the number
            m_MyNumber++;
            //[Display](Display.html) the number so far with the message
            [Debug.Log](Debug.Log.html)("First Added : " + m_MyNumber);
        }  
      
        void MySecondFunction()
        {
            //Change the [Color](Color.html) of the [GameObject](GameObject.html)
            m_Renderer.material.color = [Color.blue](Color-blue.html);
            //Ouput the message that the second function was played
            [Debug.Log](Debug.Log.html)("Second Added");
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

