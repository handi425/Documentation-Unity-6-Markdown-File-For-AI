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

# ProjectSearch

class in UnityEditor.SearchService

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

Use this API to perform searches in the Project. Engines for this type of
search implement the
[IProjectSearchEngine](SearchService.IProjectSearchEngine.html) interface.

Registered Project search engines are called during searches in the Project
browser. When the default object selector is used, they are also called for
Asset searches.  
  
The following example creates a Project search engine:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.SearchService;
    using UnityEngine;
    using Object = UnityEngine.Object;  
      
    [ProjectSearchEngine]
    class TestProjectSearchEngine : [IProjectSearchEngine](SearchService.IProjectSearchEngine.html)
    {
        public string name => "My Custom Engine";  
      
        public void BeginSession([ISearchContext](SearchService.ISearchContext.html) context)
        {
        }  
      
        public void EndSession([ISearchContext](SearchService.ISearchContext.html) context)
        {
        }  
      
        public void BeginSearch([ISearchContext](SearchService.ISearchContext.html) context, string query)
        {
        }  
      
        public void EndSearch([ISearchContext](SearchService.ISearchContext.html) context)
        {
        }  
      
        public IEnumerable<string> Search([ISearchContext](SearchService.ISearchContext.html) context, string query, [Action](Unity.Android.Gradle.Manifest.Action.html)<IEnumerable<string>> asyncItemsReceived)
        {
            var allPaths = AssetDatabase.GetAllAssetPaths();
            var filteredPaths = allPaths.Where(path => !path.StartsWith("Library")).Where(path => path.IndexOf(query, StringComparison.InvariantCultureIgnoreCase) >= 0).ToList();
            return filteredPaths;
        }
    }
    

Additional resources:
[ProjectSearchEngineAttribute](SearchService.ProjectSearchEngineAttribute.html),
[IProjectSearchEngine](SearchService.IProjectSearchEngine.html).

### Static Properties

[EngineScope](SearchService.ProjectSearch.EngineScope.html)| A enum that
indicates the search scope for ProjectSearch engines. It is used by
ProjectSearchContext.  
---|---  
  
### Static Methods

[RegisterEngine](SearchService.ProjectSearch.RegisterEngine.html)| Registers a
Project search engine dynamically.  
---|---  
[UnregisterEngine](SearchService.ProjectSearch.UnregisterEngine.html)|
Unregisters a dynamically registered engine.  
  
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

