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

#  [SceneManager](SceneManagement.SceneManager.html).LoadScene

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

public static void LoadScene(int sceneBuildIndex,
[SceneManagement.LoadSceneMode](SceneManagement.LoadSceneMode.html) mode =
LoadSceneMode.Single);

## Declaration

public static void LoadScene(string sceneName,
[SceneManagement.LoadSceneMode](SceneManagement.LoadSceneMode.html) mode =
LoadSceneMode.Single);

### Parameters

sceneName | Name or path of the Scene to load.  
---|---  
sceneBuildIndex | Index of the Scene in the Build Settings to load.  
mode | Allows you to specify whether or not to load the Scene additively. See [LoadSceneMode](SceneManagement.LoadSceneMode.html) for more information about the options.  
  
### Description

Loads the Scene by its name or index in Build Settings.

**Note:** In most cases, to avoid pauses or performance hiccups while loading,
you should use the asynchronous version of this command which is:
[LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html).  
  
When using
[SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html), the
scene loads in the next frame, that is it does not load immediately. This
semi-asynchronous behavior can cause frame stuttering and can be confusing
because load does not complete immediately.  
  
Because loading is set to complete in the next rendered frame, calling
[SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html) forces
all previous AsyncOperations to complete, even if
[AsyncOperation.allowSceneActivation](AsyncOperation-
allowSceneActivation.html) is set to false. To avoid this, use
[LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html) instead.  
  
The given `sceneName` can either be the Scene name only, without the `.unity`
extension, or the path as shown in the BuildSettings window still without the
`.unity` extension. If only the Scene name is given this will load the first
Scene in the list that matches. If you have multiple Scenes with the same name
but different paths, you should use the full path.  
  
Note that `sceneName` is case insensitive, except when you load the Scene from
an [AssetBundle](AssetBundle.html).  
  
For opening Scenes in the Editor see
[EditorSceneManager.OpenScene](SceneManagement.EditorSceneManager.OpenScene.html).
`SceneA` can additively load `SceneB` multiple times. The regular name is used
for each loaded scene. If `SceneA` loads `SceneB` ten times each `SceneB` will
have the same name. Finding a particular added scene is not possible.  
  
If a single mode scene is loaded, Unity calls Resources.UnloadUnusedAssets
automatically.

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Only specifying the sceneName or sceneBuildIndex will load the [Scene](SceneManagement.Scene.html) with the Single mode
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("OtherSceneName", [LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html));
        }
    }
    
    
    
    // Load an assetbundle which contains Scenes.
    // When the user clicks a button the first [Scene](SceneManagement.Scene.html) in the assetbundle is
    // loaded and replaces the current [Scene](SceneManagement.Scene.html).  
      
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class LoadScene : [MonoBehaviour](MonoBehaviour.html)
    {
        private [AssetBundle](AssetBundle.html) myLoadedAssetBundle;
        private string[] scenePaths;  
      
        // Use this for initialization
        void Start()
        {
            myLoadedAssetBundle = [AssetBundle.LoadFromFile](AssetBundle.LoadFromFile.html)("Assets/AssetBundles/scenes");
            scenePaths = myLoadedAssetBundle.GetAllScenePaths();
        }  
      
        void OnGUI()
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 100, 30), "Change [Scene](SceneManagement.Scene.html)"))
            {
                [Debug.Log](Debug.Log.html)("Scene2 loading: " + scenePaths[0]);
                [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)(scenePaths[0], [LoadSceneMode.Single](SceneManagement.LoadSceneMode.Single.html));
            }
        }
    }
    

The following two script examples show how
[LoadScene](SceneManagement.SceneManager.LoadScene.html) can load Scenes from
Build Settings. `LoadSceneA` uses the name of the Scene to load. `LoadSceneB`
uses the number of the Scene to load. The scripts work together.  
  
`LoadSceneA` file.

    
    
    // SceneA.
    // SceneA is given the sceneName which will
    // load SceneB from the Build [Settings](Rendering.RayTracingAccelerationStructure.Settings.html)  
      
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class LoadScenesA : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)("LoadSceneA");
        }  
      
        public void LoadA(string scenename)
        {
            [Debug.Log](Debug.Log.html)("sceneName to load: " + scenename);
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)(scenename);
        }
    }
    

`LoadSceneB` file.

    
    
    // SceneB.
    // SceneB is given the sceneBuildIndex of 0 which will
    // load SceneA from the Build [Settings](Rendering.RayTracingAccelerationStructure.Settings.html)  
      
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class LoadScenesB : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)("LoadSceneB");
        }  
      
        public void LoadB(int sceneANumber)
        {
            [Debug.Log](Debug.Log.html)("sceneBuildIndex to load: " + sceneANumber);
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)(sceneANumber);
        }
    }
    

* * *

## Declaration

public static [SceneManagement.Scene](SceneManagement.Scene.html)
LoadScene(int sceneBuildIndex,
[SceneManagement.LoadSceneParameters](SceneManagement.LoadSceneParameters.html)
parameters);

## Declaration

public static [SceneManagement.Scene](SceneManagement.Scene.html)
LoadScene(string sceneName,
[SceneManagement.LoadSceneParameters](SceneManagement.LoadSceneParameters.html)
parameters);

### Parameters

sceneName | Name or path of the Scene to load.  
---|---  
sceneBuildIndex | Index of the Scene in the Build Settings to load.  
parameters | Various parameters used to load the Scene.  
  
### Returns

**Scene** A handle to the Scene being loaded.

### Description

Loads the Scene by its name or index in Build Settings.

An example using two scenes called `Scene1` and `Scene2`. ExampleScript1.cs is
for `scene1` and ExampleScript2.cs is for `scene2`.

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    // This is scene1.  It loads 3 copies of scene2.
    // Each copy has the same name.  
      
    public class ExampleScript1 : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Scene](SceneManagement.Scene.html) scene;  
      
        private void Start()
        {
            var parameters = new [LoadSceneParameters](SceneManagement.LoadSceneParameters.html)([LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html));  
      
            scene = [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("scene2", parameters);
            [Debug.Log](Debug.Log.html)("Load 1 of scene2: " + scene.name);
            scene = [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("scene2", parameters);
            [Debug.Log](Debug.Log.html)("Load 2 of scene2: " + scene.name);
            scene = [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("scene2", parameters);
            [Debug.Log](Debug.Log.html)("Load 3 of scene2: " + scene.name);
        }
    }
    

Scene2:

    
    
    using UnityEngine;  
      
    // create a randomly placed cube  
      
    public class ExampleScript2 : [MonoBehaviour](MonoBehaviour.html)
    {
        private void Start()
        {
            [GameObject](GameObject.html) cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            cube.transform.position = new [Vector3](Vector3.html)([Random.Range](Random.Range.html)(-5.0f, 5.0f), 0.0f, [Random.Range](Random.Range.html)(-5.0f, 5.0f));
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

