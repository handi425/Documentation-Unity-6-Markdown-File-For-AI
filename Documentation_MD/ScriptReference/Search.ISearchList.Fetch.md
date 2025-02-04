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

#  [ISearchList](Search.ISearchList.html).Fetch

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

public IEnumerable<SearchItem> Fetch();

### Returns

**IEnumerable <SearchItem>** List of search items. Items can be null and must
be discarded.

### Description

Yields search items until the search query is finished.

Nullified items can be returned while the search request is pending.

    
    
    [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/[Request](PackageManager.Requests.Request.html) List")]
    public static void RequestList()
    {
        [ISearchList](Search.ISearchList.html) results = [SearchService.Request](Search.SearchService.Request.html)("*.cs");
    
        // It is important to note that when you request some search results,
        // that you need to enumerate them asynchronously using the returned search list.
        AsyncResultEnumerator.Fetch(results, item => [Debug.Log](Debug.Log.html)(item));
    }
    
    struct AsyncResultEnumerator
    {
        private [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> m_OnEnumerate;
        private IEnumerator<[SearchItem](Search.SearchItem.html)> m_Iterator;
    
        public static AsyncResultEnumerator Fetch([ISearchList](Search.ISearchList.html) results, [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> onEnumerate)
        {
            return new AsyncResultEnumerator(results, onEnumerate);
        }
    
        public AsyncResultEnumerator([ISearchList](Search.ISearchList.html) results, [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> onEnumerate)
        {
            m_OnEnumerate = onEnumerate;
            m_Iterator = results.GetEnumerator();
            [EditorApplication.update](EditorApplication-update.html) += EnumerateResults;
        }
    
        private void EnumerateResults()
        {
            if (m_Iterator == null || !m_Iterator.MoveNext())
            {
                m_Iterator = null;
                [EditorApplication.update](EditorApplication-update.html) -= EnumerateResults;
            }
            else if (m_Iterator.Current != null)
                m_OnEnumerate(m_Iterator.Current);
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

