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

#  [Application](Application.html).streamingAssetsPath

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

public static string streamingAssetsPath;

### Description

The path to the `StreamingAssets` folder (Read Only).

Use the `StreamingAssets` folder to store assets. At runtime,
`Application.streamingAssetsPath` provides the path to the folder. Add the
asset name to `Application.streamingAssetsPath`. The built application can
load the asset at this address. You can use the [Debug.Log](Debug.Log.html)
class to print the path to the `StreamingAssets` folder to the Unity Console.  
  
You cannot use synchronous filesystem APIs, such as the C# `System.IO.File`
class, to access the `StreamingAssets` folder on the WebGL and Android
platforms. No file access is available on WebGL. Android uses a compressed
`.apk` file. These platforms return a URL. Use the
[UnityWebRequest](Networking.UnityWebRequest.html) class to access the assets.

    
    
    using UnityEngine;
    using System.IO;
    using UnityEngine.Video;  
      
    // [Application](Application.html)-streamingAssetsPath example.
    //
    // Play a video and let the user stop/start it.
    // The video location is StreamingAssets. The video is
    // played on the camera background.  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private UnityEngine.Video.VideoPlayer videoPlayer;
        private string status;  
      
        void Start()
        {
            [GameObject](GameObject.html) cam = [GameObject.Find](GameObject.Find.html)("Main [Camera](Camera.html)");
            videoPlayer = cam.AddComponent<UnityEngine.Video.VideoPlayer>();  
      
            // Obtain the location of the video clip.
            videoPlayer.url = Path.Combine([Application.streamingAssetsPath](Application-streamingAssetsPath.html), "SampleVideo_1280x720_5mb.mp4");  
      
            // Restart from beginning when done.
            videoPlayer.isLooping = true;  
      
            // Do not show the video until the user needs it.
            videoPlayer.Pause();  
      
            status = "Press to play";
        }  
      
        void OnGUI()
        {
            [GUIStyle](GUIStyle.html) buttonWidth = new [GUIStyle](GUIStyle.html)(GUI.skin.GetStyle("button"));
            buttonWidth.fontSize = 18 * ([Screen.width](Screen-width.html) / 800);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)([Screen.width](Screen-width.html) / 16, [Screen.height](Screen-height.html) / 16, [Screen.width](Screen-width.html) / 3, [Screen.height](Screen-height.html) / 8), status, buttonWidth))
            {
                if (videoPlayer.isPlaying)
                {
                    videoPlayer.Pause();
                    status = "Press to play";
                }
                else
                {
                    videoPlayer.Play();
                    status = "Press to pause";
                }
            }
        }
    }
    

The following code example demonstrates how to access a file in the
`StreamingAssets` folder on Android platform.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Threading.Tasks;  
      
    public class LoadStreamingAsset : [MonoBehaviour](MonoBehaviour.html)
    {
        async void Start()
        {
            string filePath = System.IO.Path.Combine([Application.streamingAssetsPath](Application-streamingAssetsPath.html), "filetoload.txt");  
      
            [UnityWebRequest](Networking.UnityWebRequest.html) request = [UnityWebRequest.Get](Networking.UnityWebRequest.Get.html)(filePath);
            [UnityWebRequestAsyncOperation](Networking.UnityWebRequestAsyncOperation.html) operation = request.SendWebRequest();  
      
            while (!operation.isDone)
            {
                await Task.Yield();
            }  
      
            if (request.result == [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
            {
                [Debug.Log](Debug.Log.html)(request.downloadHandler.text);
            }
            else
            {
                [Debug.LogError](Debug.LogError.html)("Cannot load file at " + filePath);
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

