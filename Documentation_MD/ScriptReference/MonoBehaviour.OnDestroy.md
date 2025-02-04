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

#  [MonoBehaviour](MonoBehaviour.html).OnDestroy()

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

Destroying the attached Behaviour will result in the game or Scene receiving
[OnDestroy](MonoBehaviour.OnDestroy.html).

[OnDestroy](MonoBehaviour.OnDestroy.html) occurs when a Scene or game ends.
Stopping the Play mode when running from inside the Editor will end the
application. As this end happens an [OnDestroy](MonoBehaviour.OnDestroy.html)
will be executed. Also, if a Scene is closed and a new Scene is loaded the
[OnDestroy](MonoBehaviour.OnDestroy.html) call will be made.  
When built as a standalone application
[OnDestroy](MonoBehaviour.OnDestroy.html) calls are made when Scenes end. A
Scene ending typically means a new Scene is loaded.  
  
**Note:** [OnDestroy](MonoBehaviour.OnDestroy.html) will only be called on
game objects that have previously been active.  
  
  
  
In the following scripts the behaviour of
[OnDestroy](MonoBehaviour.OnDestroy.html) is shown. When running inside
`ExampleClass1` a button is available. Using this button calls
[OnDestroy](MonoBehaviour.OnDestroy.html) and then switches to
`ExampleClass2`. Once `ExampleClass2` is active
[OnDestroy](MonoBehaviour.OnDestroy.html) will be used when the application is
closed. If `ExampleClass1` quits by closing the application it will call
[OnDestroy](MonoBehaviour.OnDestroy.html). (In the build and run of the
application the console displays the text output to the Player Log.)  
  
**Warning** : If the user suspends your application on a mobile platform, the
operating system can quit the application to free up resources. In this case,
depending on the operating system, Unity might be unable to call this method.
On mobile platforms, it is best practice to not rely on this method to save
the state of your application. Instead, consider every loss of application
focus as the exit of the application and use
[MonoBehaviour.OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) to
save any data.

    
    
    using UnityEngine;
    using UnityEngine.UI;
    using UnityEngine.SceneManagement;  
      
    public class ExampleClass1 : [MonoBehaviour](MonoBehaviour.html)
    {
        private float timePass = 0.0f;
        private int updateCount = 0;  
      
        void Start()
        {
            [Debug.Log](Debug.Log.html)("Start1");
        }  
      
        // code that generates a message every second
        void [Update](PlayerLoop.Update.html)()
        {
            timePass += [Time.deltaTime](Time-deltaTime.html);  
      
            if (timePass > 1.0f)
            {
                timePass = 0.0f;
                [Debug.Log](Debug.Log.html)("Update1: " + updateCount);
                updateCount = updateCount + 1;
            }
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 250, 60), "Change to scene2"))
            {
                [Debug.Log](Debug.Log.html)("Exit1");
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)(1);
            }
        }  
      
        // generate a message before the Start() function
        void OnEnable()
        {
            [Debug.Log](Debug.Log.html)("OnEnable1");
        }  
      
        // generate a message when the game shuts down or switches to another [Scene](SceneManagement.Scene.html)
        // or switched to ExampleClass2
        void OnDestroy()
        {
            [Debug.Log](Debug.Log.html)("OnDestroy1");
        }
    }
    

ExampleClass2:

    
    
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class ExampleClass2 : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)("Start2");
        }  
      
        void OnEnable()
        {
            [Debug.Log](Debug.Log.html)("OnEnable2");
        }  
      
        // generate a message when the game shuts down
        void OnDestroy()
        {
            [Debug.Log](Debug.Log.html)("OnDestroy2");
        }
    }
    

[OnDestroy](MonoBehaviour.OnDestroy.html) cannot be a co-routine.

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

