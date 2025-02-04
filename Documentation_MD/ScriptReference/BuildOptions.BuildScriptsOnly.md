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

#  [BuildOptions](BuildOptions.html).BuildScriptsOnly

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

### Description

Only build the scripts in a Project.

Before you can use [BuildScriptsOnly](BuildOptions.BuildScriptsOnly.html), you
need to build the whole Project. Then you can run builds that only have script
changes. Rebuilding the player data will be skipped for faster iteration
speed.  
  
Platforms which support the incremental build pipeline will automatically run
scripts only builds if Unity detects that the data files have not changed,
even if [BuildScriptsOnly](BuildOptions.BuildScriptsOnly.html) is not used.
You can still use [BuildScriptsOnly](BuildOptions.BuildScriptsOnly.html) to
force a script only build and ignore any pending player data changes.  
  
The following script example uses
[BuildScriptsOnly](BuildOptions.BuildScriptsOnly.html). The script builds the
entire Project initially. After you've run the script for the first time, you
can use the script to only compile the script changes. To use the script
create a project and add the Editor script and the game script below.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class EditorExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Build/Build scripts")]
        public static void MyBuild()
        {
            [BuildPlayerOptions](BuildPlayerOptions.html) buildPlayerOptions = new [BuildPlayerOptions](BuildPlayerOptions.html)();
            buildPlayerOptions.scenes = new[] { "Assets/scene.unity" };
            buildPlayerOptions.locationPathName = "scriptBuilds";
            buildPlayerOptions.target = [BuildTarget.StandaloneOSX](BuildTarget.StandaloneOSX.html);  
      
            // use these options for the first build
            buildPlayerOptions.options = [BuildOptions.Development](BuildOptions.Development.html);  
      
            // use these options for building scripts
            // buildPlayerOptions.options = [BuildOptions.BuildScriptsOnly](BuildOptions.BuildScriptsOnly.html) | [BuildOptions.Development](BuildOptions.Development.html);  
      
            [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
        }
    }
    

Attach the following simple script to an empty GameObject in the scene:

    
    
    using UnityEngine;  
      
    // Change the camera to the usual blue color and display a label.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Camera](Camera.html) cam;  
      
        void Awake()
        {
            cam = [Camera.main](Camera-main.html);
            cam.clearFlags = [CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html);
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(100, 100, 100, 50), "ExampleClass");
        }
    }
    

Now run the `Build/Build scripts` example. This builds an executable. Run that
executable and a dark blue window with the label appears. Next add some cubes
and spheres to the Project. Make the following script changes:

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Camera](Camera.html) cam;  
      
        // added line
        private float delay;  
      
        void Awake()
        {
            delay = 0.0f;
            cam = [Camera.main](Camera-main.html);
            cam.clearFlags = [CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html);
        }  
      
        // added script code
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            delay = delay + [Time.deltaTime](Time-deltaTime.html);  
      
            if (delay > 0.5f)
            {
                cam.backgroundColor = new [Color](Color.html)(0.0f, 0.0f, [Random.Range](Random.Range.html)(0.0f, 0.25f));
                delay = 0.0f;
            }
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(100, 100, 100, 50), "ExampleClass");
        }
    }
    

Finally, swap the commented lines in the `EditorExample` script:

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class EditorExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Build/Build scripts")]
        public static void MyBuild()
        {
            [BuildPlayerOptions](BuildPlayerOptions.html) buildPlayerOptions = new [BuildPlayerOptions](BuildPlayerOptions.html)();
            buildPlayerOptions.scenes = new[] { "Assets/scene.unity" };
            buildPlayerOptions.locationPathName = "scriptBuilds";
            buildPlayerOptions.target = [BuildTarget.StandaloneOSX](BuildTarget.StandaloneOSX.html);  
      
            // use these options for the first build
            // buildPlayerOptions.options = [BuildOptions.Development](BuildOptions.Development.html);  
      
            // use these options for building scripts
            buildPlayerOptions.options = [BuildOptions.BuildScriptsOnly](BuildOptions.BuildScriptsOnly.html) | [BuildOptions.Development](BuildOptions.Development.html);  
      
            [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html)(buildPlayerOptions);
        }
    }
    

Use the `Build/Build scripts` to regenerate the application and then launch
it. The application will now show random changes to the background color.
However the added cubes and spheres are not visible.

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

