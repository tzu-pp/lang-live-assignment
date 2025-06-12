import csv
from itertools import chain

try:
    import parser
except ImportError:
    print("ERROR: 'parser.py' module not found.")
    exit(1)
except Exception as e:
    print(f"ERROR: Failed to import parser module: {e}")
    exit(1)


if __name__ == "__main__":
    # run each parsing function and combine data
    all_streamers_sources = []
    
    parsing_functions = [
        ("last live", parser.parse_last_live),
        ("hot", parser.parse_hot),
        ("class list", parser.parse_class_list),
        ("rank list", parser.parse_rank_list)
    ]
    
    for source_name, parse_func in parsing_functions:
        try:
            data = parse_func()
            all_streamers_sources.append(data)
        except Exception as e:
            print(f"WARNING: Failed to parse '{source_name}' data: {e}")

    all_streamers = chain(*all_streamers_sources)


    # filter pfid between 4000000 ~ 5000000 and remove duplicates from raw data
    filtered_streamers = []
    seen_pfid= set()
    min_pfid, max_pfid = 4000000, 5000000

    for streamer_type, pfid, nickname in all_streamers:
        try:
            # print(f"[{streamer_type}] {pfid}: {nickname}")

            assert min_pfid <= int(pfid) <= max_pfid, f"pfid {pfid} out of range"
            
            if pfid not in seen_pfid:
                seen_pfid.add(pfid)
                filtered_streamers.append((pfid, nickname))
        except ValueError:
            print(f"WARNING: Invalid pfid '{pfid}' for {nickname}")
        except AssertionError:
            continue
        except Exception as e:
            print(f"ERROR: Processing streamer {pfid} {nickname}: {e}")



    # save filtered streamers result to csv file
    output_filename = "filtered_streamers.csv"
    try:
        with open(output_filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["pfid", "Nickname"])   # header row
            for pfid, nickname in filtered_streamers:
                writer.writerow([pfid, nickname])
        print(f"The result saved to {output_filename} successfully.")
   
    except IOError as e:
        print(f"ERROR: File operation failed: {e}")
    except Exception as e: 
        print(f"ERROR: Saving file failed: {e}")


