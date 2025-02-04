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

# AssetBundle

class in UnityEngine

/

Inherits from:[Object](Object.html)

/

Implemented
in:[UnityEngine.AssetBundleModule](UnityEngine.AssetBundleModule.html)

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

API for accessing the content of AssetBundle files.

This class exposes an API, via static methods, for loading and managing
AssetBundles.  
  
This same class offers non-static methods and properties that expose the
contents of a specific loaded AssetBundle, including the ability to load an
Asset from within an AssetBundle.  
  
Create AssetBundles by calling
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html) or
using the [Addressables
package](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html).
The build process generates one or more AssetBundle files, and each
AssetBundle file contains a serialized instance of this class.  
  
Note: AssetBundle.LoadAsset, and the other Load methods, do not support
loading Scenes from AssetBundles. Instead, in runtime you load the streamed
scene AssetBundle and then call
[SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html) or
[SceneManager.LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html)
with the Scene name. In the Editor it is not supported to load Scenes from
AssetBundles so calls to
[EditorSceneManager.OpenScene](SceneManagement.EditorSceneManager.OpenScene.html)
will fail with an error that the Scene file is not found.  
  
Additional resources: [Intro to
AssetBundles](../Manual/AssetBundlesIntro.html),
[UnityWebRequestAssetBundle.GetAssetBundle](Networking.UnityWebRequestAssetBundle.GetAssetBundle.html),
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html).

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.Networking;  
      
    public class SampleBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Start()
        {
            var uwr = [UnityWebRequestAssetBundle.GetAssetBundle](Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)("https://myserver/myBundle.unity3d");
            yield return uwr.SendWebRequest();  
      
            // Get an asset from the bundle and instantiate it.
            [AssetBundle](AssetBundle.html) bundle = [DownloadHandlerAssetBundle.GetContent](Networking.DownloadHandlerAssetBundle.GetContent.html)(uwr);
            var loadAsset = bundle.LoadAssetAsync<[GameObject](GameObject.html)>("Assets/Players/MainPlayer.prefab");
            yield return loadAsset;  
      
            Instantiate(loadAsset.asset);  
      
            bundle.Unload(true);
        }
    }
    

### Static Properties

[memoryBudgetKB](AssetBundle-memoryBudgetKB.html)| Controls the size of the
shared AssetBundle loading cache. Default value is 1MB.  
---|---  
  
### Properties

[isStreamedSceneAssetBundle](AssetBundle-isStreamedSceneAssetBundle.html)|
Return true if the AssetBundle contains Unity Scene files  
---|---  
  
### Public Methods

[Contains](AssetBundle.Contains.html)| Check if an AssetBundle contains a
specific object.  
---|---  
[GetAllAssetNames](AssetBundle.GetAllAssetNames.html)| Return all Asset names
in the AssetBundle.  
[GetAllScenePaths](AssetBundle.GetAllScenePaths.html)| Return all the names of
Scenes in the AssetBundle.  
[LoadAllAssets](AssetBundle.LoadAllAssets.html)| Loads all Assets contained in
the AssetBundle synchronously.  
[LoadAllAssetsAsync](AssetBundle.LoadAllAssetsAsync.html)| Loads all Assets
contained in the AssetBundle asynchronously.  
[LoadAsset](AssetBundle.LoadAsset.html)| Synchronously loads an Asset from the
AssetBundle.  
[LoadAssetAsync](AssetBundle.LoadAssetAsync.html)| Asynchronously loads an
Asset from the bundle.  
[LoadAssetWithSubAssets](AssetBundle.LoadAssetWithSubAssets.html)| Loads Asset
and sub Assets from the AssetBundle synchronously.  
[LoadAssetWithSubAssetsAsync](AssetBundle.LoadAssetWithSubAssetsAsync.html)|
Loads Asset and sub Assets from the AssetBundle asynchronously.  
[Unload](AssetBundle.Unload.html)| Unloads an AssetBundle freeing its data.  
[UnloadAsync](AssetBundle.UnloadAsync.html)| Unloads assets in the bundle.  
  
### Static Methods

[GetAllLoadedAssetBundles](AssetBundle.GetAllLoadedAssetBundles.html)| Get an
enumeration of all the currently loaded AssetBundles.  
---|---  
[LoadFromFile](AssetBundle.LoadFromFile.html)| Synchronously loads an
AssetBundle from a file on disk.  
[LoadFromFileAsync](AssetBundle.LoadFromFileAsync.html)| Asynchronously loads
an AssetBundle from a file on disk.  
[LoadFromMemory](AssetBundle.LoadFromMemory.html)| Synchronously load an
AssetBundle from a memory region.  
[LoadFromMemoryAsync](AssetBundle.LoadFromMemoryAsync.html)| Asynchronously
load an AssetBundle from a memory region.  
[LoadFromStream](AssetBundle.LoadFromStream.html)| Synchronously loads an
AssetBundle from a managed Stream.  
[LoadFromStreamAsync](AssetBundle.LoadFromStreamAsync.html)| Asynchronously
loads an AssetBundle from a managed Stream.  
[RecompressAssetBundleAsync](AssetBundle.RecompressAssetBundleAsync.html)|
Asynchronously recompress a downloaded/stored AssetBundle from one
BuildCompression to another.  
[UnloadAllAssetBundles](AssetBundle.UnloadAllAssetBundles.html)| Unloads all
currently loaded AssetBundles.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

