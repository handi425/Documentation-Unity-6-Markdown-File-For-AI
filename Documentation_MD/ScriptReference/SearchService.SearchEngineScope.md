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

# SearchEngineScope

enumeration

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

An enumeration that contains the available search engine scopes.

A search engine scope identifies where a search comes from. This is useful
when implementing a single entry point for the base engine functions:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SearchService;
    
    class BaseEngine : [ISearchEngineBase](SearchService.ISearchEngineBase.html)
    {
        public virtual void BeginSession([ISearchContext](SearchService.ISearchContext.html) context)
        {
            if (context.engineScope == [ObjectSelectorSearch.EngineScope](SearchService.ObjectSelectorSearch.EngineScope.html) || context.engineScope == [ProjectSearch.EngineScope](SearchService.ProjectSearch.EngineScope.html))
            {
                // [Cache](Cache.html) Assets.
            }
            if (context.engineScope == [ObjectSelectorSearch.EngineScope](SearchService.ObjectSelectorSearch.EngineScope.html) || context.engineScope == [SceneSearch.EngineScope](SearchService.SceneSearch.EngineScope.html))
            {
                // [Cache](Cache.html) [Scene](SceneManagement.Scene.html) objects.
            }
        }
    
        public virtual void EndSession([ISearchContext](SearchService.ISearchContext.html) context)
        {
            // Flush any cached data.
        }
    
        public virtual void BeginSearch([ISearchContext](SearchService.ISearchContext.html) context, string query)
        {
        }
    
        public virtual void EndSearch([ISearchContext](SearchService.ISearchContext.html) context)
        {
        }
    
        public string name => "My Engine [Service](Unity.Android.Gradle.Manifest.Service.html)";
    }
    
    [SceneSearchEngine]
    class SampleSceneFilterEngine : BaseEngine, [ISceneSearchEngine](SearchService.ISceneSearchEngine.html)
    {
        public bool Filter([ISearchContext](SearchService.ISearchContext.html) context, string query, HierarchyProperty objectToFilter)
        {
            // Use cached [Scene](SceneManagement.Scene.html) objects.
            // ...
            return true;
        }
    }
    
    [ProjectSearchEngine]
    class SampleProjectSearchEngine : BaseEngine, [IProjectSearchEngine](SearchService.IProjectSearchEngine.html)
    {
        public IEnumerable<string> Search([ISearchContext](SearchService.ISearchContext.html) context, string query, [Action](Unity.Android.Gradle.Manifest.Action.html)<IEnumerable<string>> asyncItemsReceived)
        {
            // Use cached Assets.
            // ...
            return new List<string>();
        }
    }
    
    [ObjectSelectorEngine]
    class SampleObjectSelectorEngine : BaseEngine, [IObjectSelectorEngine](SearchService.IObjectSelectorEngine.html)
    {
        public bool SelectObject([ISearchContext](SearchService.ISearchContext.html) context, [Action](Unity.Android.Gradle.Manifest.Action.html)<UnityEngine.Object, bool> onObjectSelectorClosed, [Action](Unity.Android.Gradle.Manifest.Action.html)<UnityEngine.Object> onObjectSelectedUpdated)
        {
            // Use cached Assets and [Scene](SceneManagement.Scene.html) objects.
            return true;
        }
    
        public void SetSearchFilter([ISearchContext](SearchService.ISearchContext.html) context, string searchFilter)
        {}
    }
    

### Properties

[Scene](SearchService.SearchEngineScope.Scene.html)| Identifies a search for
Scene engines.  
---|---  
[Project](SearchService.SearchEngineScope.Project.html)| Identifies a search
for Project engines.  
[ObjectSelector](SearchService.SearchEngineScope.ObjectSelector.html)|
Identifies a search for ObjectSelector engines.  
  
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

