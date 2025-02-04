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

#  [SearchUtils](Search.SearchUtils.html).FetchGameObjects

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

public static GameObject[]
FetchGameObjects([SceneManagement.Scene](SceneManagement.Scene.html) scene);

## Declaration

public static IEnumerable<GameObject> FetchGameObjects();

### Parameters

scene | Scene to get objects from.  
---|---  
  
### Returns

**GameObject[]** The array of game objects in the scene.

### Description

Utility function to fetch all the game objects in a particular scene.

Use `SearchUtils.FetchGameObjects` to create a custom
[SearchProvider](Search.SearchProvider.html) that is able to access current
scene objects.

    
    
    static void OnEnable()
    {
        s_GameObjects = [SearchUtils.FetchGameObjects](Search.SearchUtils.FetchGameObjects.html)().ToArray();
        s_QueryEngine = new [QueryEngine](Search.QueryEngine.html)<[GameObject](GameObject.html)>();
    
        // Id supports all operators
        s_QueryEngine.AddFilter("id", go => go.GetInstanceID());
        // Name supports only :, = and !=
        s_QueryEngine.AddFilter("n", go => go.name, new[] {":", "=", "!="});
    
        // Add distance filtering. Does not support :.
        s_QueryEngine.AddFilter("dist", DistanceHandler, DistanceParamHandler, new[] {"=", "!=", "<", ">", "<=", ">="});
    }
    
    
    
    static IEnumerator SearchItems([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider)
    {
        var query = s_QueryEngine.ParseQuery(context.searchQuery);
        if (!query.valid)
            yield break;
    
        var filteredObjects = query.Apply(s_GameObjects);
        foreach (var filteredObject in filteredObjects)
        {
            yield return provider.CreateItem(filteredObject.GetInstanceID().ToString(), null, null, null, filteredObject.GetInstanceID());
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

