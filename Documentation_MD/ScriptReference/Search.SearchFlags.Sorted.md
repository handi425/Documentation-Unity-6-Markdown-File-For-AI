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

#  [SearchFlags](Search.SearchFlags.html).Sorted

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

Fetched items are sorted by the search service.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    public class SearchFlags_Sorted
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchFlags](Search.SearchFlags.html)/Sorted")]
        public static void RequestAll()
        {
            [ISearchList](Search.ISearchList.html) results = [SearchService.Request](Search.SearchService.Request.html)("p: t:Script", [SearchFlags.Sorted](Search.SearchFlags.Sorted.html));
            AsyncResultEnumerator.Fetch(results, item => [Debug.Log](Debug.Log.html)(item));
        }
    
        struct AsyncResultEnumerator
        {
            private [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> m_OnEnumerate;
            private IEnumerator<[SearchItem](Search.SearchItem.html)> m_Iterator;
            private [ISearchList](Search.ISearchList.html) m_SearchList;
    
            public static AsyncResultEnumerator Fetch([ISearchList](Search.ISearchList.html) results, [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> onEnumerate)
            {
                return new AsyncResultEnumerator(results, onEnumerate);
            }
    
            public AsyncResultEnumerator([ISearchList](Search.ISearchList.html) results, [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> onEnumerate)
            {
                m_OnEnumerate = onEnumerate;
                m_SearchList = results;
                m_Iterator = results.GetEnumerator();
                [EditorApplication.update](EditorApplication-update.html) += WaitForSearchCompleted;
            }
    
            private void WaitForSearchCompleted()
            {
                // Wait for the search to complete, otherwise it will not yield sorted items.
                if (!m_SearchList.pending)
                {
                    [EditorApplication.update](EditorApplication-update.html) -= WaitForSearchCompleted;
                    [EditorApplication.update](EditorApplication-update.html) += EnumerateResults;
                }
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

