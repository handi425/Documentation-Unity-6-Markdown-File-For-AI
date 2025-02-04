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

#  [AsyncOperation](AsyncOperation.html).progress

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

public float progress;

### Description

What's the operation's progress. (Read Only)

Return an operation's progress. (Read Only) This returns how close the
operation is to finishing. The operation is finished when the progress float
reaches 1.0 and isDone is called. If you set allowSceneActivation to false,
progress is halted at 0.9 until it is set to true. This is extremely useful
for creating loading bars.  
  
Additional resources: [isDone](AsyncOperation-isDone.html).

    
    
    //This script lets you load a [Scene](SceneManagement.Scene.html) asynchronously. It uses an asyncOperation to calculate the progress and outputs the current progress to Text (could also be used to make progress bars).  
      
    //Attach this script to a [GameObject](GameObject.html)
    //Create a [Button](UIElements.Button.html) (**Create** >**UI** >**Button**) and a Text [GameObject](GameObject.html) (**Create** >**UI** >**Text**) and attach them both to the Inspector of your [GameObject](GameObject.html)
    //In Play [Mode](Scripting.GarbageCollector.Mode.html), press your [Button](UIElements.Button.html) to load the [Scene](SceneManagement.Scene.html), and the Text changes depending on progress. Press the space key to activate the [Scene](SceneManagement.Scene.html).
    //**Note:** The progress may look like it goes straight to 100% if your [Scene](SceneManagement.Scene.html) doesn’t have a lot to load.  
      
    using System.Collections;
    using UnityEngine;
    using UnityEngine.SceneManagement;
    using UnityEngine.UI;  
      
    public class AsyncOperationProgressExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public Text m_Text;
        public [Button](UIElements.Button.html) m_Button;  
      
        void Start()
        {
            //Call the LoadButton() function when the user clicks this [Button](UIElements.Button.html)
            m_Button.onClick.AddListener(LoadButton);
        }  
      
        void LoadButton()
        {
            //Start loading the [Scene](SceneManagement.Scene.html) asynchronously and output the progress bar
            StartCoroutine(LoadScene());
        }  
      
        IEnumerator LoadScene()
        {
            yield return null;  
      
            //Begin to load the [Scene](SceneManagement.Scene.html) you specify
            [AsyncOperation](AsyncOperation.html) asyncOperation = [SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html)("Scene3");
            //Don't let the [Scene](SceneManagement.Scene.html) activate until you allow it to
            asyncOperation.allowSceneActivation = false;
            [Debug.Log](Debug.Log.html)("Pro :" + asyncOperation.progress);
            //When the load is still in progress, output the Text and progress bar
            while (!asyncOperation.isDone)
            {
                //Output the current progress
                m_Text.text = "Loading progress: " + (asyncOperation.progress * 100) + "%";  
      
                // Check if the load has finished
                if (asyncOperation.progress >= 0.9f)
                {
                    //Change the Text to show the [Scene](SceneManagement.Scene.html) is ready
                    m_Text.text = "Press the space bar to continue";
                    //Wait to you press the space key to activate the [Scene](SceneManagement.Scene.html)
                    if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
                        //Activate the [Scene](SceneManagement.Scene.html)
                        asyncOperation.allowSceneActivation = true;
                }  
      
                yield return null;
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

