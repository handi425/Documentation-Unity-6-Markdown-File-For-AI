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

#  [SearchProvider](Search.SearchProvider.html).fetchColumns

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

public Func<SearchContext,IEnumerable<SearchItem>,IEnumerable<SearchColumn>>
fetchColumns;

### Description

Handler used to enumerate search columns to be used in the Search Table view.

See [SearchColumnProviderAttribute](Search.SearchColumnProviderAttribute.html)
if you need to define new column formats to display your custom values.

    
    
    static IEnumerable<[SearchColumn](Search.SearchColumn.html)> FetchColumns([SearchContext](Search.SearchContext.html) context, IEnumerable<[SearchItem](Search.SearchItem.html)> items)
    {
        yield return new [SearchColumn](Search.SearchColumn.html)("Performance/[Sample](PackageManager.UI.Sample.html) Count", "count", nameof(PerformanceMetric));
        yield return new [SearchColumn](Search.SearchColumn.html)("Performance/Peak [Time](Time.html)", "peak", nameof(PerformanceMetric));
        yield return new [SearchColumn](Search.SearchColumn.html)("Performance/Average [Time](Time.html)", "avg", nameof(PerformanceMetric));
        yield return new [SearchColumn](Search.SearchColumn.html)("Performance/Total [Time](Time.html)", "total", nameof(PerformanceMetric));
    }  
      
    [SearchColumnProvider(nameof(PerformanceMetric))]
    public static void PerformanceMetric([SearchColumn](Search.SearchColumn.html) column)
    {
        column.getter = args =>
        {
            switch (column.selector)
            {
                case "count": return EditorPerformanceTracker.GetSampleCount(args.item.id);
                case "peak": return EditorPerformanceTracker.GetPeakTime(args.item.id);
                case "avg": return EditorPerformanceTracker.GetAverageTime(args.item.id);
                case "total": return EditorPerformanceTracker.GetTotalTime(args.item.id);
                case "age": return EditorPerformanceTracker.GetTimestamp(args.item.id);
            }  
      
            return null;
        };  
      
        if (column.selector != "count")
        {
            column.drawer = args =>
            {
                [GUI.Label](GUI.Label.html)(args.rect, GetTimeLabel((double)args.value, 0.5d, 2.0d), [ItemSelectors.GetItemContentStyle](Search.ItemSelectors.GetItemContentStyle.html)(column));
                return args.value;
            };
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

