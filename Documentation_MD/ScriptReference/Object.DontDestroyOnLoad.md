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

#  [Object](Object.html).DontDestroyOnLoad

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

[Switch to Manual](../Manual/class-Object.html "Go to Object Component in the
Manual")

## Declaration

public static void DontDestroyOnLoad([Object](Object.html) target);

### Parameters

target | An Object not destroyed on [Scene](SceneManagement.Scene.html) change.  
---|---  
  
### Description

Do not destroy the target Object when loading a new
[Scene](SceneManagement.Scene.html).

The load of a new [Scene](SceneManagement.Scene.html) destroys all current
[Scene](SceneManagement.Scene.html) objects. Call
[Object.DontDestroyOnLoad](Object.DontDestroyOnLoad.html) to preserve an
Object during scene loading. If the target Object is a component or
[GameObject](GameObject.html), Unity also preserves all of the
[Transform](Transform.html)’s children.
[Object.DontDestroyOnLoad](Object.DontDestroyOnLoad.html) only works for root
GameObjects or components on root GameObjects.
[Object.DontDestroyOnLoad](Object.DontDestroyOnLoad.html) does not return a
value.  
  
The following example script uses
[Object.DontDestroyOnLoad](Object.DontDestroyOnLoad.html). The example has
`scene1` which starts playing background music from an
[AudioSource](AudioSource.html). The music continues when `scene2` loads.
Switch between scenes using a button.  
  
To implement this example, create two new
[Scene](SceneManagement.Scene.html)s, named `scene1` and `scene2`. Open
`scene1` and add the `SceneSwap.cs` script to an empty
[GameObject](GameObject.html) and name it `Menu`. Next, add `DontDestroy.cs`
to a new [GameObject](GameObject.html) and name it `BackgroundMusic`. Add an
[AudioSource](AudioSource.html) to `BackgroundMusic` \- `Add Component > Audio
> Audio Source` \- and import an [AudioClip](AudioClip.html) into your
Project. Assign the [AudioClip](AudioClip.html) to the
[AudioSource](AudioSource.html)’s [AudioClip](AudioClip.html) field. Create a
tag, call it `music`, and add it to `BackgroundMusic`. Switch to `scene2`.
Again add `SceneSwap.cs` to a new [GameObject](GameObject.html) and name it
`Menu`. Save the Project. Return to `scene1` and run the Project from the
`Editor`.  
  
`SceneSwap.cs` script:

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    // [Object.DontDestroyOnLoad](Object.DontDestroyOnLoad.html) example.
    //
    // Two scenes call each other. This happens when OnGUI button is clicked.
    // scene1 will load scene2; scene2 will load scene1. Both scenes have
    // the [Menu](Menu.html) [GameObject](GameObject.html) with the SceneSwap.cs script attached.
    //
    // [AudioSource](AudioSource.html) plays an [AudioClip](AudioClip.html) as the game runs. This is on the
    // BackgroundMusic [GameObject](GameObject.html) which has a music tag.  The audio
    // starts in [AudioSource.playOnAwake](AudioSource-playOnAwake.html). The DontDestroy.cs script
    // is attached to BackgroundMusic.  
      
    public class SceneSwap : [MonoBehaviour](MonoBehaviour.html)
    {
        private void OnGUI()
        {
            int xCenter = ([Screen.width](Screen-width.html) / 2);
            int yCenter = ([Screen.height](Screen-height.html) / 2);
            int width = 400;
            int height = 120;  
      
            [GUIStyle](GUIStyle.html) fontSize = new [GUIStyle](GUIStyle.html)(GUI.skin.GetStyle("button"));
            fontSize.fontSize = 32;  
      
            [Scene](SceneManagement.Scene.html) scene = [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)();  
      
            if (scene.name == "scene1")
            {
                // Show a button to allow scene2 to be switched to.
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(xCenter - width / 2, yCenter - height / 2, width, height), "Load second scene", fontSize))
                {
                    [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("scene2");
                }
            }
            else
            {
                // Show a button to allow scene1 to be returned to.
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(xCenter - width / 2, yCenter - height / 2, width, height), "Return to first scene", fontSize))
                {
                    [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("scene1");
                }
            }
        }
    }
    

`DontDestroy.cs` script:

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [Object.DontDestroyOnLoad](Object.DontDestroyOnLoad.html) example.
    //
    // This script example manages the playing audio. The [GameObject](GameObject.html) with the
    // "music" tag is the BackgroundMusic [GameObject](GameObject.html). The [AudioSource](AudioSource.html) has the
    // audio attached to the [AudioClip](AudioClip.html).  
      
    public class DontDestroy : [MonoBehaviour](MonoBehaviour.html)
    {
        void Awake()
        {
            [GameObject](GameObject.html)[] objs = [GameObject.FindGameObjectsWithTag](GameObject.FindGameObjectsWithTag.html)("music");  
      
            if (objs.Length > 1)
            {
                Destroy(this.gameObject);
            }  
      
            DontDestroyOnLoad(this.gameObject);
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

